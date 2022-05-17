from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Room, RoomImage


class RoomDetailView(DetailView):
    model = Room
    template_name = 'room/room_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room_photos'] = RoomImage.objects.filter(room=self.object)
        return context


class RoomListView(ListView):
    model = Room
    template_name = 'room/room_list.html'