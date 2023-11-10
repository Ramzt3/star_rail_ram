from django.shortcuts import get_object_or_404, render
from .models import Character, LightCone, Element

def index(request):
    return render(request, 'core/index.html')

def characters(request):
    characters = Character.objects.all().order_by('-rarity', 'name')
    elements = Element.objects.all()

    return render(request, 'core/characters.html', {
        'characters': characters,
        'elements': elements
    })

def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk) 

    return render(request, 'core/character_detail.html', {
        'character': character
    })

    return render
def light_cones(request):
    light_cones = LightCone.objects.all()

    return render(request, 'core/light_cones.html', {
        'light_cones': light_cones
    })

def light_cone_detail(request, pk):
    light_cone = get_object_or_404(LightCone, pk=pk) 

    return render(request, 'core/light_cone_detail.html', {
        'light_cone': light_cone 
    })
