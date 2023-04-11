from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title_text = models.CharField(max_length=100, verbose_name="Заголовок")
    title_map = models.CharField(max_length=100, verbose_name="Название на карте")
    description_short = models.TextField(verbose_name="Короткое описание")
    description_long = HTMLField(verbose_name="Длинное описание")
    lng = models.FloatField(verbose_name="Долгота координаты")
    lat = models.FloatField(verbose_name="Широта координаты")

    def __str__(self):
        return self.title_text

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"


class Image(models.Model):
    place = models.ForeignKey(to="places.Place", verbose_name="Место", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Картинка")
    number = models.IntegerField(default=0, db_index=True, verbose_name="Позиция")

    def __str__(self):
        return f"{self.number} {self.place}"

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
        ordering = ["number"]
