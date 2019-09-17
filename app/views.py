from rest_framework import generics
from .models import Music
from .serializers import MusicSerializer
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.forms import ModelForm


# Create your views here.
class MusicList(generics.ListCreateAPIView):
    model = Music
    # template_name = ".html"
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class MusicView(DetailView):
    model = Music
    
class MusicCreate(CreateView):
    model = Music
    fields = ['title', 'seconds']
    success_url = reverse_lazy('music_list')

class MusicUpdate(UpdateView):
    model = Music
    fields = ['title', 'seconds']
    success_url = reverse_lazy('music_list')

class MusicDelete(DeleteView):
    model = Music
    success_url = reverse_lazy('music_list')