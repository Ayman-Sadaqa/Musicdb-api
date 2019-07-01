
from django.contrib import admin
from django.urls import path
from webapp.views import AlbumsList, SongsList, ArtistList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('albums/', AlbumsList, name='final'),
    path('artist/', ArtistList, name='final'),
    path('songs/', SongsList, name='final'),
]
