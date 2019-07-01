import uuid
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models


class Artist(models.Model):
    artistName = models.SlugField()
    artistType = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=1)
    artistId = models.PositiveIntegerField(default=uuid.uuid4, unique=True)
    content_artist = GenericForeignKey('artistType', 'artistId')

    def __str__(self):
        return "%s %s" % (self.artistName, self.artistId)


class Album(models.Model):
    albumName = models.SlugField()
    albumType = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=1)
    albumId = models.PositiveIntegerField(default=uuid.uuid4, unique=True)
    content_album = GenericForeignKey('albumType', 'albumId')
    Artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.albumName

    class Meta:
        ordering = ('albumName',)


class Song(models.Model):
    songName = models.SlugField()
    songType = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=1)
    songId = models.PositiveIntegerField(default=uuid.uuid4, unique=True)
    content_song = GenericForeignKey('songType', 'songId')
    Album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.songName

    class Meta:
        ordering = ('songName',)

