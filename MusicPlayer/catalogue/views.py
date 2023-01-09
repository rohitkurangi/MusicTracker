# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Track, Album
from .serializers import TrackSerializer
from django.shortcuts import get_object_or_404


# Create your views here.

class TrackView(APIView):
    def get(self, request):
        # result = Track.objects.get(id=id)
        # if id:
        #     serializers = TrackSerializer(result)
        #     return Response({'success': 'success', "students": serializers.data}, status=200)
        result = Track.objects.order_by('priority')
        serializers = TrackSerializer(result, many=True)
        return Response({'status': 'success', "students": serializers.data}, status=200)

    def post(self, request):
        serializer = TrackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        result = Track.objects.filter(id=str(id))
        album_name = request.data.get("album_name")
        try:
            album_obj = Album.objects.get(album_name=album_name, is_active=True)
        except:
            return Response({"status": "error", "data":"album_obj not available"})
        if result:
            request.data["album_name"]=album_obj.id
            serializer = TrackSerializer(result[0], data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        result = get_object_or_404(Track, id=id)
        result.delete()
        return Response({"status": "success", "data": "Record Deleted"})