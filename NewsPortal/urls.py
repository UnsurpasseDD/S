from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news_portal.urls')),
    path('accounts/', include('allauth.urls')),
    path('sign/', include('sign.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('news_portal.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]
