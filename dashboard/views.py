from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Character, LightCone


@login_required(login_url="core:login")
def dashboard(request):
    total_characters = Character.objects.count()
    total_light_cones = LightCone.objects.count()

    return render(request, 'dashboard/dashboard.html', {
        'total_characters': total_characters,
        'total_light_cones': total_light_cones,
    })
