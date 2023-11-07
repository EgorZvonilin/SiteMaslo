from django.shortcuts import render
from .models import Advertisement, Otzivi
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def maslo(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'maslo.html', context)

def otzivi2(request):
    otzivi = Otzivi.objects.all()
    context = {'otzivi': otzivi}
    return render(request, 'otzivi2.html', context)

def dostavka(request):
    return render(request, 'dostavka.html')

def kontakti(request):
    return render(request, 'kontakti.html')

def photo(request):
    return render(request, 'photo.html')

# Create your views here.
