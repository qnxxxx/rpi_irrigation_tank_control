from django.shortcuts import render
from .models import WaterLevel


# Create your views here.
def water_level_graph_view(request):
    levels = WaterLevel.objects.all()
    for level in levels:
        level.timestamp = level.timestamp.strftime("%Y-%m-%d %H:%M:%S")

    context = {
        'levels': levels
    }

    return render(request, 'water_level/water_level_graph.html', context)
