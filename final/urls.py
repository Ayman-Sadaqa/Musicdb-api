from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from webapp.views import AlbumsList, SongsList, ArtistList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('albums/', AlbumsList, name='final'),
    path('artists/', ArtistList, name='final'),
    path('songs/', SongsList, name='final'),
]
