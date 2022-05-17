from django.db import models

# Create your models here.
from django.urls import reverse


class Room(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    cost = models.PositiveIntegerField('Цена')
    address = models.CharField('Адрес', max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('room_detail', kwargs={'pk': self.pk})

    def get_primary_photo(self):
        return RoomImage.objects.get(room=self, primary=True).image

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class RoomImage(models.Model):
    image = models.ImageField('Изображение', upload_to='room_photo')
    room = models.ForeignKey(Room, verbose_name='Комната', on_delete=models.CASCADE)
    primary = models.BooleanField('Главное фото')

    def __str__(self):
        rent_obj = self.room.title
        return f"Фото - {rent_obj} - {self.pk}"

    class Meta:
        verbose_name = 'Фото комнаты'
        verbose_name_plural = 'Фото комнаты'