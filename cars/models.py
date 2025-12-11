# B:\ИС-4\carsharing\cars\models.py
from django.db import models


class CarCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Категория авто"
        verbose_name_plural = "Категории авто"
        ordering = ['name']

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    year = models.PositiveIntegerField(blank=True, null=True)
    # ДОБАВЛЕНО ПОЛЕ КАТЕГОРИИ ↓
    category = models.ForeignKey(
        CarCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="cars",
        verbose_name="Категория"
    )
    image = models.ImageField(
        upload_to='cars/',
        blank=False,
        null=True
    )
    is_available = models.BooleanField(default=True, verbose_name="Доступен")

    class Meta:
        ordering = ['name']
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

    def __str__(self):
        if self.year:
            return f"{self.name} ({self.year}) - {self.price}"
        return f"{self.name} - {self.price}"


class CarCharacteristics(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    value = models.CharField(max_length=100, verbose_name="Значение")
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name="characteristics",
        verbose_name="Автомобиль"
    )

    class Meta:
        verbose_name = "Характеристика авто"
        verbose_name_plural = "Характеристики авто"

    def __str__(self):
        return f"{self.name}: {self.value}"
