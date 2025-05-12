# myapp/views.py

from django.shortcuts import render # type: ignore
from .models import Diploma

def index(request):
    diplomas = Diploma.objects.all()  # Получаем все объекты Diploma
    return render(request, 'myapp/index.html', {'diplomas': diplomas})