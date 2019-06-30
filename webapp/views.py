from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Album
from .serializers import AlbumSerializer
from .models import Artist
from .serializers import ArtistSerializer
from .models import Song
from .serializers import SongSerializer


@api_view(["GET"])
def AlbumsList(request):
    Album1 = Album.objects.all()
    serializer = AlbumSerializer(Album1, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def SongsList(request):
    Song1 = Song.objects.all()
    serializer = SongSerializer(Song1, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def ArtistList(request):
    Artist1 = Artist.objects.all()
    serializer = ArtistSerializer(Artist1, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
