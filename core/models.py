from django.db import models


class Element(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Path(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    rarity = models.IntegerField()
    path = models.ForeignKey(Path, related_name='characters', on_delete=models.CASCADE)
    element = models.ForeignKey(Element, related_name='characters', on_delete=models.CASCADE)
    craeted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class LightCone(models.Model):
    name = models.CharField(max_length=100)
    rarity = models.IntegerField()
    path = models.ForeignKey(Path, related_name='light_cones', on_delete=models.CASCADE)
    element = models.ForeignKey(Element, related_name='light_cones', on_delete=models.CASCADE)
    craeted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
