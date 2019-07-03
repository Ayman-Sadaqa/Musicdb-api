import graphene
from graphene_django import DjangoObjectType, DjangoConnectionField
from webapp.models import Album, Artist, Song


class SongType(DjangoObjectType):
    class Meta:
        interfaces = [graphene.relay.Node]
        model = Song


class AlbumType(DjangoObjectType):
    class Meta:
        interfaces = [graphene.relay.Node]
        model = Album


class ArtistType(DjangoObjectType):
    class Meta:
        interfaces = [graphene.relay.Node]
        model = Artist


class Query(graphene.ObjectType):
    songs = DjangoConnectionField(SongType)
    albums = DjangoConnectionField(AlbumType)
    artists = DjangoConnectionField(ArtistType)

    def resolver_all_songs(self, info, **kwargs):
        return Song.objects.all()

    def resolver_all_albums(self, info, **kwargs):
        return Album.objects.all()

    def resolver_all_artist(self, info, **kwargs):
        return Artist.objects.all()


schema = graphene.Schema(query=Query)
