from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    product_type =[
        ('Cap','Capsules'),
        ('Pow','Powders'),
        ('Tab','Tablets'),
        ('Liq','Liquids'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')
    description = models.TextField()
    type = models.CharField(max_length=3, choices=product_type)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name