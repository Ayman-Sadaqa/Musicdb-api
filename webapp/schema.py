import graphene
from graphene_django import DjangoObjectType, DjangoConnectionField
from webapp.models import Album, Artist, Song


class SongType(DjangoObjectType):
    class Meta:
        interfaces = [graphene.relay.Node]
        model = Song


class CreateSong(graphene.Mutation):
    class Input:
        song_name = graphene.String()

    ok = graphene.Boolean()
    song = graphene.Field(SongType)

    @staticmethod
    def mutate(self, args, content, info):
        song = Song(songName=args.get('song_name'))
        ok = True
        return CreateSong(ok=ok, song=song)


class Mutation(graphene.ObjectType):
    create_song = CreateSong.Field()


#################################################


class AlbumType(DjangoObjectType):
    class Meta:
        interfaces = [graphene.relay.Node]
        model = Album


class CreateAlbum(graphene.Mutation):
    class Input:
        albumName = graphene.String()
        Artist = graphene.String()

    ok = graphene.Boolean()
    album = graphene.Field(AlbumType)

    @staticmethod
    def mutate(self, args, content, info):
        album = Album(albumName=args.get('albumName'))
        ok = True
        return CreateAlbum(ok=ok, album=album)


class Mutation(graphene.ObjectType):
    create_album = CreateAlbum.Field()

################################################


class ArtistType(DjangoObjectType):
    class Meta:
        interfaces = [graphene.relay.Node]
        model = Artist


class CreateArtist(graphene.Mutation):
    class Input:
        artistName = graphene.String()

    ok = graphene.Boolean()
    artist = graphene.Field(ArtistType)

    @staticmethod
    def mutate(self, args, content, info):
        artist = Artist(artistName=args.get('artistName'))
        ok = True
        return CreateArtist(ok=ok, artist=artist)


class Mutation(graphene.ObjectType):
    create_artist = CreateArtist.Field()


##################################################


class Query(graphene.ObjectType):
    songs = DjangoConnectionField(SongType, songName=graphene.String())
    albums = DjangoConnectionField(AlbumType, albumName=graphene.String())
    artists = DjangoConnectionField(ArtistType, artistsName=graphene.String())

    @graphene.resolve_only_args
    def resolve_songs(self, **kwargs):
        if kwargs == {}:
            return Song.objects.all()
        return Song.objects.first(pk=kwargs.get('songName'))

    @graphene.resolve_only_args
    def resolve_albums(self, **kwargs):
        if kwargs == {}:
            return Album.objects.all()
        return Album.objects.first(pk=kwargs.get('albumName'))

    @graphene.resolve_only_args
    def resolve_artists(self, **kwargs):
        if kwargs == {}:
            return Artist.objects.all()
        return Artist.objects.first(pk=kwargs.get('artistsName'))


