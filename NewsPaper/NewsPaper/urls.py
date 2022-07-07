from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('', include('startpage.urls')),
   path('auth/', include('allauth.urls')),
   path('admin/', admin.site.urls),
   path('accounts/', include('accounts.urls')),
   path('pages/', include('django.contrib.flatpages.urls')),
   path('news/', include('news.urls')),
]
