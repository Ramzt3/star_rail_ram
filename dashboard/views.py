from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import Character, LightCone
from dashboard.forms import AddCharacterForm, AddLightConeForm


@login_required(login_url="core:login")
def dashboard(request):
    total_characters = Character.objects.count()
    total_light_cones = LightCone.objects.count()

    return render(request, 'dashboard/dashboard.html', {
        'total_characters': total_characters,
        'total_light_cones': total_light_cones,
    })


@login_required(login_url="core:login")
def add_character(request):
    form = AddCharacterForm()

    if request.method == 'POST':
        form = AddCharacterForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('dashboard:add-characters')

    return render(request, 'dashboard/add_character.html', {
        'form': form
    })


@login_required(login_url="core:login")
def add_light_cone(request):
    form = AddLightConeForm()

    if request.method == 'POST':
        form = AddLightConeForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('dashboard:add-light-cone')

    return render(request, 'dashboard/add_light_cone.html', {
        'form': form
    })
