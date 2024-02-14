from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-character', views.add_character, name='add-character'),
    path('add-light-cone', views.add_light_cone, name='add-light-cone'),
]
