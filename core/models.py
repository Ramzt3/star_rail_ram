from django.db import models


class Gender(models.Model):
    gender = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "gender"

    def __str__(self):
        return self.gender


class Rarity(models.Model):
    star = models.CharField(max_length=1)

    class Meta:
        verbose_name_plural = "rarities"

    def __str__(self):
        return self.star


class Element(models.Model):
    name = models.CharField(max_length=30)
    icon = models.ImageField(upload_to="media/icons/elements/", null=True, blank=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Path(models.Model):
    name = models.CharField(max_length=30)
    icon = models.ImageField(upload_to="media/icons/paths/", null=True, blank=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=100)
    gender = models.ForeignKey(Gender, related_name='characters', on_delete=models.CASCADE)
    rarity = models.ForeignKey(Rarity, related_name='characters', on_delete=models.CASCADE)
    path = models.ForeignKey(Path, related_name='characters', on_delete=models.CASCADE)
    element = models.ForeignKey(Element, related_name='characters', on_delete=models.CASCADE)
    craeted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class LightCone(models.Model):
    name = models.CharField(max_length=100)
    rarity = models.ForeignKey(Rarity, related_name='light_cones', on_delete=models.CASCADE)
    path = models.ForeignKey(Path, related_name='light_cones', on_delete=models.CASCADE)
    element = models.ForeignKey(Element, related_name='light_cones', on_delete=models.CASCADE)
    craeted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
