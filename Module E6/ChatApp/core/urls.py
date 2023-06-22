from django.urls import path

from .views import index, room, rooms_return


urlpatterns = [
    path('', index, name="index"),
    path('roomsupdate/', rooms_return, name="rooms_return"),
    path('<str:room_name>/', room, name="room"),
]
