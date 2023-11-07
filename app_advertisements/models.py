from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model

timezone.now()

User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена за 100 мл', max_digits=10, decimal_places=2)
    price2 = models.DecimalField('Цена за 250 мл', max_digits=10, decimal_places=2)
    price3 = models.DecimalField('Цена за 500 мл', max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='advertisements/')

    def __str__(self):
        return f"Advertisements(id={self.id}, title={self.title})"

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style = "color: green; font-weight: bold">Сегодня в {}</span>', created_time
            )
        else:
            return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Дата изменения')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            created_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style = "color: orange; font-weight: bold">Сегодня в {}</span>', created_time
            )
        else:
            return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Фото')
    def get_html_image(self):
        if self.image:
            return format_html(
                '<img src="{url}" style="max-width: 80px; max-height: 80px;"', url=self.image.url
            )

class Otzivi(models.Model):
    title = models.CharField('Пользователь', max_length=128)
    description = models.TextField('Отзыв')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Otzivi(id={self.id}, title={self.title})"

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style = "color: green; font-weight: bold">Сегодня в {}</span>', created_time
            )
        else:
            return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

class Meta:
    db_table = "advertisements"


# Create your models here.
