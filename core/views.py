from django.shortcuts import render
from .models import Character

def index(request):
    return render(request, 'core/index.html')

def characters(request):
    characters = Character.objects.all()

    return render(request, 'core/characters.html', {
        'characters': characters
    })
