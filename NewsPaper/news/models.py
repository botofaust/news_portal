from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def update_rating(user):
        rating_posts = Post.objects.filter(author__pk=user.pk).aggregate(Sum('rating'))['rating__sum'] * 3
        rating_comments = Comment.objects.filter(user__pk=user.pk).aggregate(Sum('rating'))['rating__sum']
        rating_views = Comment.objects.filter(post__author__pk=user.pk).aggregate(Sum('rating'))['rating__sum']
        user.rating = rating_posts + rating_comments + rating_views
        user.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    post_news = 'Новость'
    post_article = 'Статья'
    POST_TYPES = [('NS', post_news), ('AT', post_article)]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=2, choices=POST_TYPES)
    create_datetime = models.DateTimeField(auto_now_add=True)
    lastchange_datetime = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    caption = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.caption

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        result = self.text[:124] + '...'
        return result

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])


class PostCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    create_datetime = models.DateTimeField(auto_now_add=True)
    lastchange_datetime = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
