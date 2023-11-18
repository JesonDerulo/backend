from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.TextField(null=True, blank=True)
    stock_quantity = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name
    