from django.shortcuts import render
from django.conf import settings

DEBUG = False

# Create your views here.


def home_screen_view(request, *args, **kwargs):
    context = dict()
    context['debug_mode'] = settings.DEBUG
    context['debug'] = DEBUG
    context['room_id'] = '1'
    return render(request, 'core/home.html', context)
