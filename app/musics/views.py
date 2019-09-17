from rest_framework import generics
from .models import Music
from .serializers import MusicSerializer
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.forms import ModelForm


# Create your views here.
# class MusicList(generics.ListCreateAPIView):
#     model = Music
#     # template_name = ".html"
#     queryset = Music.objects.all()
#     serializer_class = MusicSerializer

# class MusicView(DetailView):
#     model = Music
    
# class MusicCreate(CreateView):
#     model = Music
#     fields = ['title', 'seconds']
#     success_url = reverse_lazy('music_list')

# class MusicUpdate(UpdateView):
#     model = Music
#     fields = ['title', 'seconds']
#     success_url = reverse_lazy('music_list')

# class MusicDelete(DeleteView):
#     model = Music
#     success_url = reverse_lazy('music_list')

class MusicForm(ModelForm):
    class Meta:
        model = Music
        fields = ['title', 'seconds']

def music_list(request, template_name='musics/music_list.html'):
    music = Music.objects.all()
    data = {}
    data['object_list'] = music
    return render(request, template_name, data)

def music_view(request, pk, template_name='musics/music_detail.html'):
    music= get_object_or_404(Music, pk=pk)    
    return render(request, template_name, {'object':music})

def music_create(request, template_name='musics/music_form.html'):
    form = MusicForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('music_list')
    return render(request, template_name, {'form':form})

def music_update(request, pk, template_name='musics/music_form.html'):
    music= get_object_or_404(Music, pk=pk)
    form = MusicForm(request.POST or None, instance=music)
    if form.is_valid():
        form.save()
        return redirect('music_list')
    return render(request, template_name, {'form':form})

def music_delete(request, pk, template_name='musics/music_confirm_delete.html'):
    music= get_object_or_404(Music, pk=pk)    
    if request.method=='POST':
        music.delete()
        return redirect('music_list')
    return render(request, template_name, {'object':music})