from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.search_artist, name='search_artist')
]
