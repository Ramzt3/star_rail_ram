from django.contrib import admin
from .models import Element, Path, Character, LightCone

# Register your models here.
admin.site.register(Element)
admin.site.register(Path)
admin.site.register(Character)
admin.site.register(LightCone)
