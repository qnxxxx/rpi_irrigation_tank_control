from django.urls import path

from water_level.views import (
    water_level_graph_view,
)

app_name = 'water_level'

urlpatterns = [
    path('graph', water_level_graph_view, name='graph')
]
