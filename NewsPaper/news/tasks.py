from celery import shared_task
from .models import Post


@shared_task
def weekly_mailing():
    Post.mailing()


@shared_task
def post_send(post_pk):
    post = Post.objects.get(pk=post_pk)
    post.send_email_to_subs()
