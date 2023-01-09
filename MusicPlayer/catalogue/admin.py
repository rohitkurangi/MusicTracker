from django.contrib import admin

# Register your models here.
from catalogue.models import Artist, Track,Album

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Track)