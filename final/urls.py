from django.contrib import admin
from django.urls import path
from webapp.views import AlbumsList, SongsList, ArtistList
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('albums/', AlbumsList, name='final'),
    path('artists/', ArtistList, name='final'),
    path('songs/', SongsList, name='final'),
    path('graphql/', GraphQLView.as_view(graphiql=True))
]
