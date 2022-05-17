from django.urls import path
from . import views

urlpatterns = [
    path('room/<int:pk>', views.RoomDetailView.as_view(), name='room_detail'),
    path('rooms/', views.RoomListView.as_view(), name='room_list'),
]