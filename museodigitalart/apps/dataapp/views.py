from django.shortcuts import render

# Create your views here.

from .models import Tema

def home(request):
    temi = Tema.objects.all()
    return render(request, 'main/home.html', {'temi': temi})