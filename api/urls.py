from django.urls import path
from . import views

urlpatterns = [
    path('rooms', views.RoomsAPIView.as_view(), name='rooms'),
]