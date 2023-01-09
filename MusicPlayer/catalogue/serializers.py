from rest_framework import serializers
from .models import Track,Album


class TrackSerializer(serializers.ModelSerializer):
    track_name = serializers.CharField(max_length=200, required=True)
    priority = serializers.IntegerField(required=True)
    album_name = serializers.CharField(source='album.album_name')
    album_id = serializers.CharField(source='album.id',required=False)
    artist = serializers.CharField(source='album.artist.artist_name',required=False)

    class Meta:
        model = Track
        fields = ('id','track_name','priority','album_name','album_id','artist')

    def create(self, validated_data):
        print(validated_data,"ssss")
        """
        Create and return a new `Students` instance, given the validated data.
        """
        album = validated_data.pop('album')
        album_name=album.get("album_name")
        try:
            album_obj = Album.objects.get(album_name=album_name,is_active=True)
        except:
            album_obj = Album.objects.get(**validated_data)
        return Track.objects.create(**validated_data,album=album_obj)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Students` instance, given the validated data.
        """
        instance.track_name = validated_data.get('track_name', instance.track_name)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.album = validated_data.get('album_name', instance.album)
        instance.save()
        return instance