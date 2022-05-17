from rest_framework.generics import ListCreateAPIView
from applications.room.models import Room
from .serializers import RoomSerializer


class RoomsAPIView(ListCreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()