
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='game_images/')
    youtube_link = models.URLField()
    download_link = models.URLField()
    #download_link = models.FileField(upload_to='torrents/')
    def __str__(self):
        return self.title
