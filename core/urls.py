from django.urls import path
from core.views import index, characters, light_cones, character_detail, light_cone_detail

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('characters', characters, name='characters'),
    path('characters/<int:pk>', character_detail, name='character_detail'),
    path('light_cones/', light_cones, name='light_cones'),
    path('light_cones/<int:pk>', light_cone_detail, name='light_cone_detail'),
]
