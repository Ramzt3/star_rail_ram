from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.my_login, name='login'),
    path('register/', views.register, name='register'),
    path('user-logout/', views.user_logout, name='user-logout'),
    path('characters', views.characters, name='characters'),
    path('characters/<int:pk>', views.character_detail, name='character-detail'),
    path('light-cones/', views.light_cones, name='light-cones'),
    path('light-cones/<int:pk>', views.light_cone_detail, name='light-cone-detail'),
]
