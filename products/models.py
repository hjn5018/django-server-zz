from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    
    CATEGORY_CHOICES = (
        ('F', 'Fruit'),
        ('V', 'Vegetable'),
        ('M', 'Meat'),
        ('O', 'Other'),
    )
    
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
