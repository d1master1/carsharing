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
    is_available = models.BooleanField(default=True)

    category = models.ForeignKey(
        CarCategory,
        on_delete=models.CASCADE,
        related_name='cars',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        if self.year:
            return f"{self.name} ({self.year}) - {self.price}"
        return f"{self.name} - {self.price}"


class CarCharacteristics(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name="characteristics"
    )

    class Meta:
        verbose_name = "Характеристика авто"
        verbose_name_plural = "Характеристики авто"

    def __str__(self):
        return f"{self.name}: {self.value}"
