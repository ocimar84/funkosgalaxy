# No arquivo models.py

from django.db import models

# Modelo para representar as categorias dos produtos
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Modelo para representar os produtos
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name
