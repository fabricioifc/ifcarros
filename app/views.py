from rest_framework import generics
from .models import Music
from .serializers import MusicSerializer
from django.shortcuts import render

# Create your views here.
class MusicList(generics.ListCreateAPIView):
    # model = MusicList
    # template_name = ".html"
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
