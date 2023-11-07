from django.contrib import admin
from .models import Advertisement, Otzivi

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'price2', 'price3', 'created_date', 'updated_date', 'image', 'get_html_image']

class OtziviAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_date']

admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(Otzivi, OtziviAdmin)

# Register your models here.
