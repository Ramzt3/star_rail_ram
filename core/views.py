from django.shortcuts import get_object_or_404, render
from .models import Character, LightCone, Element


def index(request):
    return render(request, 'core/index.html')


def characters(request):
    elements = Element.objects.all()
    query_element = request.GET.get('element')

    if not query_element:
        characters = Character.objects.all().order_by('-rarity', 'name')
    else:
        characters = Character.objects.order_by('-rarity', 'name').filter(element=query_element)

    return render(request, 'core/characters.html', {
        'characters': characters,
        'elements': elements,
    })


def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk) 

    return render(request, 'core/character_detail.html', {
        'character': character
    })


def light_cones(request):
    elements = Element.objects.all()
    query_element = request.GET.get('element')

    if not query_element:
        light_cones = LightCone.objects.all()
    else:
        light_cones = LightCone.objects.filter(element=query_element)

    return render(request, 'core/light_cones.html', {
        'light_cones': light_cones,
        'elements': elements
    })


def light_cone_detail(request, pk):
    light_cone = get_object_or_404(LightCone, pk=pk) 

    return render(request, 'core/light_cone_detail.html', {
        'light_cone': light_cone 
    })
