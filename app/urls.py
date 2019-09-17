from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^musics/$', views.MusicList.as_view(), name='music-list'),
    # path('', views.MusicList.as_view(), name='music_list'),
    path('view/<int:pk>', views.MusicView.as_view(), name='music_view'),
    path('new', views.MusicCreate.as_view(), name='music_new'),
    path('view/<int:pk>', views.MusicView.as_view(), name='music_view'),
    path('edit/<int:pk>', views.MusicUpdate.as_view(), name='music_edit'),
    path('delete/<int:pk>', views.MusicDelete.as_view(), name='music_delete'),

]