from django.http import HttpResponse
import json
from django.shortcuts import render
from django.core.cache.backends.locmem import _caches as cache


def rooms_reader():
    rooms = []
    for key in cache['us']:
        rooms.append(key)
    return rooms


def index(request):
    rooms = rooms_reader()
    return render(request, "core/index.html", context={'rooms': rooms})


def room(request, room_name):
    room_name = room_name.replace(' ', '_')
    return render(request, "core/chatbox.html", context={"room_name": room_name})


def rooms_return(request):
    rooms = rooms_reader()
    jsn = json.dumps(rooms)
    return HttpResponse(jsn)