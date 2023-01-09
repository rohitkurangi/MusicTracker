from .views import TrackView
from django.urls import path

urlpatterns = [
    path('track/', TrackView.as_view()),
    path('track/<str:id>/', TrackView.as_view()),
    path('track/<str:id>/update/', TrackView.as_view()),
    path('track/<str:id>/delete/', TrackView.as_view())
]