from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

from . import views

urlpatterns = [
    url(r'^register$', views.register),
    url(r'^edit', views.edit),
    url(r'^follow$', views.follow),
    url(r'^unfollow$', views.unfollow),
    url(r'^search', views.search_user, name='user_search'),
    url(r'^user_search/', views.ajax_search, name='ajax_user_search'),
    url(r'^(?P<username>\w+)$', views.show_profile), 
] + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )