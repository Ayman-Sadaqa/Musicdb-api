from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models


class Artist(models.Model):
    artistName = models.CharField(max_length=20)
    artistType = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=1)
    content_artist = GenericForeignKey('artistType', 'id')

    def __str__(self):
        return self.artistName

    class Meta:
        ordering = ('artistName',)


class Album(models.Model):
    albumName = models.CharField(max_length=20)
    albumType = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=1)
    content_album = GenericForeignKey('albumType', 'id')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.albumName

    class Meta:
        ordering = ('albumName',)


class Song(models.Model):
    songName = models.CharField(max_length=20)
    songType = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=1)
    content_song = GenericForeignKey('songType', 'id')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.songName

    class Meta:
        ordering = ('songName',)

