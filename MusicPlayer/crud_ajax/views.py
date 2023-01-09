from django.shortcuts import render
from django.urls import reverse_lazy

from catalogue.models import Track, Album
    from django.views.generic import TemplateView, View, DeleteView
from django.core import serializers
from django.http import JsonResponse


class CrudView(TemplateView):
    template_name = 'crud_ajax/crud.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tracks'] = Track.objects.filter(is_active=True).order_by('priority')
        context['album'] = Album.objects.filter(is_active=True)
        temp1 = [i for i in range(1, 100)]
        temp2 = [i for i in Track.objects.values_list('priority', flat=True)]
        context['priority'] = list(set(temp1) - set(temp2))
        return context


class CreateCrudUser(View):
    def get(self, request):
        track_name = request.GET.get('name', None)
        priority = request.GET.get('address', None)
        album_id = request.GET.get('age', None)

        obj = Track.objects.create(
            track_name = track_name,
            priority = priority,
            album_id = album_id
        )

        track = {'id':str(obj.id),'track':track_name,'priority':obj.priority,'artist':obj.album.artist.artist_name,'album':obj.album.album_name}
        print(track,"000000000000000000")
        data = {
            'user': track
        }
        return JsonResponse(data)

class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        track=Track.objects.get(id=id1)
        track.is_active = False
        track.save()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class UpdateCrudUser(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        track_name = request.GET.get('name', None)
        priority = request.GET.get('address', None)
        album_id = request.GET.get('age', None)

        obj = Track.objects.get(id=id1)
        obj.track_name = track_name
        obj.priority = priority
        obj.album_id = album_id
        obj.save()


        track = {'id':str(obj.id),'track':track_name,'priority':obj.priority,'artist':obj.album.artist.artist_name,'album':obj.album.album_name}

        data = {
            'user': track
        }
        return JsonResponse(data)

class TrackMusic(TemplateView):
    template_name = 'crud_ajax/tracks.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tracks'] = Track.objects.filter(is_active=True).order_by('priority')[0]
        return context

class NextPreviousTracks(TemplateView):
    template_name = 'crud_ajax/tracks.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if kwargs.get("priority") != 0:
            if kwargs.get("event") == "next":

                obj = Track.objects.filter(priority__gt=kwargs.get("priority")).order_by('priority').first()
            else:
                obj = Track.objects.filter(priority__lt=kwargs.get("priority")).order_by('priority').last()
            if not obj:
                obj = Track.objects.get(priority=kwargs.get("priority"))

            context['tracks'] = obj
            return context

