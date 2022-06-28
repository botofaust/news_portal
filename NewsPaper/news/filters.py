import datetime

from django.forms import SelectDateWidget
from django_filters import DateFilter, CharFilter, FilterSet

from .models import Post

MONTHS = {
    1: ('янв'), 2: ('фев'), 3: ('мар'), 4: ('апр'),
    5: ('май'), 6: ('июн'), 7: ('июл'), 8: ('авг'),
    9: ('сен'), 10: ('окт'), 11: ('ноя'), 12: ('дек')
}


CUR_YEAR = datetime.date.today().year
YEARS = [i for i in range(CUR_YEAR - 9, CUR_YEAR + 2)]


class PostFilter(FilterSet):
    caption = CharFilter(lookup_expr='icontains',
                         label='Заголовок')
    create_datetime = DateFilter(lookup_expr='gt',
                                 widget=SelectDateWidget(months=MONTHS, years=YEARS),
                                 label='Опубликовано после')

    class Meta:
        model = Post
        fields = {
            'caption', 'categories', 'create_datetime'
        }
