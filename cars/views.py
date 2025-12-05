from django.shortcuts import render
from django.http import HttpResponse
from .models import Car, CarCategory

def index(request):
    """Главная страница со всеми автомобилями"""
    cars = Car.objects.all()  # ПРАВИЛЬНО - внутри функции
    context = {"cars": cars}
    return render(request, "index.html", context)  # Уточнен путь

def cars_page(request):
    """Страница с автомобилями по категориям"""
    categories = CarCategory.objects.all()
    context = {"categories": categories}
    return render(request, "cars.html", context)  # Уточнен путь

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact_us(request):
    return HttpResponse("Страница для связи с нами")
