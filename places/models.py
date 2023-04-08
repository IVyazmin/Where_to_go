from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description_short = models.TextField(verbose_name="Короткое описание")
    description_long = models.TextField(verbose_name="Длинное описание")
    lng = models.CharField(max_length=50, verbose_name="Долгота координаты")
    lat = models.CharField(max_length=50, verbose_name="Широта координаты")

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(to="places.Place", verbose_name="Место", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Фото")
    number = models.IntegerField(verbose_name="Номер")

    def __str__(self):
        return f"{self.number} {self.place}"
