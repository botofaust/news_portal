from django.urls import path
from .views import PostsList, PostDetail, PostEdit, PostDelete, PostSearchList, PostCreate

urlpatterns = [
   path('', PostsList.as_view(), name='posts'),
   path('<int:pk>', PostDetail.as_view(), name='post'),
   path('create_post', PostCreate.as_view(), name='post_create'),
   path('search', PostSearchList.as_view(), name='post_search'),
   path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]
