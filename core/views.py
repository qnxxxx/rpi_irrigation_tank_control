from django.shortcuts import render

from decouple import config

# Create your views here.


def home_screen_view(request, *args, **kwargs):
    context = dict()
    context['debug_mode'] = config('DEBUG')
    context['debug'] = config('DEBUG')
    context['room_id'] = '1'
    return render(request, 'core/home.html', context)
