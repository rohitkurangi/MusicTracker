from django.db import models
import uuid

# Create your models here.
class CommonField(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Artist(CommonField):
    artist_name = models.CharField(max_length=150, null=True, blank=True)
    def __str__(self):
        return "{0}".format(self.artist_name)


class Album(CommonField):
    album_name = models.CharField(max_length=150, null=True, blank=True)
    artist = models.ForeignKey(Artist,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return "{0}".format(self.album_name)

class Track(CommonField):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,primary_key=True)
    track_name = models.CharField(max_length=150, null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    album = models.ForeignKey(Album,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return "{0}".format(self.track_name)

