from django.forms import ModelForm
from core.models import Character, LightCone


class AddCharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ["name", "gender", "rarity", "path", "element"]


class AddLightConeForm(ModelForm):
    class Meta:
        model = LightCone
        fields = ["name", "rarity", "path", "element"]
