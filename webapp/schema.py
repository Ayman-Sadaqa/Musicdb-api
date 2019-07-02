import graphene
from graphene import relay, Connection
from graphene_django import DjangoObjectType
from webapp.models import Album, Artist, Song


class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist
        filter_fields = ['artistName', 'artistId']
        interfaces = (relay.Node,)

    @classmethod
    def get_node(self, artistName, artistId):
        return Artist.objects.get(id=artistId)


class ArtistTypeConnection(Connection):
    count = graphene.Int()

    class Meta:
        node = ArtistType

    def resolve_count(self, context, **kwargs):
        return Artist.objects.count()


##########################################


class AlbumType(DjangoObjectType):
    class Meta:
        model = Album
        filter_fields = ['albumName', 'albumId']
        interfaces = (relay.Node,)

    @classmethod
    def get_node(self, albumName, albumId):
        return Album.objects.get(id=albumId)


class AlbumTypeConnectionv(Connection):
    count = graphene.Int()

    class Meta:
        node = AlbumType

    def resolve_count(self, context, **kwargs):
        return Album.objects.count()

##########################################


class SongType(DjangoObjectType):
    class Meta:
        model = Song
        filter_fields = ['songName', 'songId']
        interfaces = (relay.Node,)

    @classmethod
    def get_node(self, songName, songId):
        return Song.objects.get(id=songId)


class SongTypeConnectionv(Connection):
    count = graphene.Int()

    class Meta:
        node = SongType

    def resolve_count(self, context, **kwargs):
        return Song.objects.count()


#########################################################


class Query(graphene.ObjectType):
    artist = relay.ConnectionField(ArtistTypeConnection, search=graphene.String())

    album = relay.ConnectionField(AlbumTypeConnectionv, search=graphene.String())

    song = relay.ConnectionField(SongTypeConnectionv, search=graphene.String())

    def resolve_artists(self, info, **kwargs):
        all = kwargs.get('all', None)
        if all:
            artist = Artist.objects.filter(url__icontains=all)
        else:
            artist = Artist.objects.all()
        return artist

    def resolve_albums(self, info, **kwargs):
        search = kwargs.get('search', None)
        if search:
            album = Album.objects.filter(url__icontains=search)
        else:
            album = Album.objects.all()
        return album

    def resolve_songs(self, info, **kwargs):
        search = kwargs.get('search', None)
        if search:
            song = Song.objects.filter(url__icontains=search)
        else:
            song = Song.objects.all()
        return song
