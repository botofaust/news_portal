from django import template


register = template.Library()


BAD_WORDS = ['авиация', 'приказ', 'переход']


@register.filter()
def censor(value: str):
    if type(value) != str:
        raise ValueError(f'Filter "censor" need str argument, given {type(value)}')
    result = value
    for bad_word in BAD_WORDS:
        result = result.replace(bad_word, bad_word[0] + '*' * (len(bad_word) - 1))
        result = result.replace(bad_word.capitalize(), bad_word[0].upper() + '*' * (len(bad_word) - 1))
    return result
