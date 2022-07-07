from django.urls import path

from .views import UserProfileUpdate, make_author

urlpatterns = [
    path('<int:pk>/update', UserProfileUpdate.as_view(), name='user_profile_update'),
    path('make_author', make_author, name='make_author')
]
