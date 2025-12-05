# B:\ИС-4\carsharing\cars\admin.py
from django.contrib import admin
from .models import Car, CarCategory, CarCharacteristics  # Исправлено: CarCategory -> CarCategory

class CarCharacteristicsInline(admin.TabularInline):
    model = CarCharacteristics
    extra = 1

class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'color', 'year', 'is_available', 'category']
    list_filter = ['is_available', 'category']
    search_fields = ['name', 'color']
    inlines = [CarCharacteristicsInline]

# Регистрация моделей с кастомизацией для Car
admin.site.register(Car, CarAdmin)
admin.site.register(CarCategory)  # Исправлено: CarCategory -> CarCategory
