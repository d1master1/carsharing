from django.db import models

# Create your models here.

class Car(models.Model):

    name = models.CharField(max_length=100)

    price = models.CharField(max_length=50)

    color = models.CharField(max_length=100)
    
    year = models.PositiveIntegerField(blank=True, null=True)
    
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} ({self.price}) - {self.color}"
