from django.db import models


class Album(models.Model):
    albumName = models.CharField(max_length=10)

    def __str__(self):
        return self.albumName


class Artist(models.Model):
    artistName = models.CharField(max_length=10)

    def __str__(self):
        return self.artistName


class Song(models.Model):
    songName = models.CharField(max_length=10)

    def __str__(self):
        return self.songName

