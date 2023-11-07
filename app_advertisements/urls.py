from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index, maslo, otzivi2, dostavka, kontakti, photo

urlpatterns = [
    path('', index, name='index'),
    path('maslo', maslo, name='maslo'),
    path('otzivi2', otzivi2, name='otzivi2'),
    path('dostavka', dostavka, name='dostavka'),
    path('kontakti', kontakti, name='kontakti'),
    path('photo', photo, name='photo')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)