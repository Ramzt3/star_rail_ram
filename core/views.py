from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from .models import Character, LightCone, Element, Path
from .forms import LoginForm, CreateUserForm, AddCharacterForm


def bucket_url():
    return 'https://star-ram-bucket.s3.amazonaws.com'


def index(request):
    c_char = Character.objects.count()
    return render(request, 'core/index.html', {
        'c_char': c_char,
    })


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print("in post")

        if form.is_valid():
            form.save()
            print("is valid")

            return redirect('core:login')

    return render(request, 'core/register.html', {
        'register_form': form
    })


def my_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("core:index")

    return render(request, 'core/login.html', {
        'login_form': form,
    })


def user_logout(request):
    auth.logout(request)

    return redirect("core:index")


def characters(request):
    main_url = bucket_url()
    elements = Element.objects.all()
    paths = Path.objects.all()
    query_element = request.GET.get('element')

    if not query_element:
        characters = Character.objects.all().order_by('-rarity', 'name')
    else:
        characters = Character.objects.order_by('-rarity', 'name').filter(element=query_element)

    return render(request, 'core/characters.html', {
        'characters': characters,
        'elements': elements,
        'paths': paths,
        'main_url': main_url,
    })


def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)

    return render(request, 'core/character_detail.html', {
        'character': character
    })


def add_character(request):
    form = AddCharacterForm()

    return render(request, 'core/add_character.html', {
        'form': form
    })


def light_cones(request):
    main_url = bucket_url()
    elements = Element.objects.all()
    query_element = request.GET.get('element')

    if not query_element:
        light_cones = LightCone.objects.all()
    else:
        light_cones = LightCone.objects.filter(element=query_element)

    return render(request, 'core/light_cones.html', {
        'light_cones': light_cones,
        'elements': elements,
        'main_url': main_url
    })


def light_cone_detail(request, pk):
    light_cone = get_object_or_404(LightCone, pk=pk)

    return render(request, 'core/light_cone_detail.html', {
        'light_cone': light_cone
    })
