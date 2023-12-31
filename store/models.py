from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Modelo para representar as categorias dos produtos
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    def __str__(self):
        return self.name

# Modelo para representar os produtos
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    favorites = models.ManyToManyField(
        User, related_name='favorites', default=None, blank=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("product_detail",args=[self.id])

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('cancel', 'Cancel'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='pending')
    street_address = models.CharField("Street Address", max_length=255, blank=True, null=True)
    city = models.CharField("City", max_length=255, blank=True, null=True)
    state = models.CharField("State", max_length=255, blank=True, null=True)
    zip_code = models.CharField("ZIP Code", max_length=10, blank=True, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='itens', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.id)

class Contact(models.Model):
    name = models.CharField("Name", max_length=255)
    email = models.EmailField("Email")
    message = models.TextField("Message")

    def __str__(self):
        return self.email


class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class Newsletter(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_date = models.DateTimeField(default=timezone.now)
    recipients = models.TextField(default="", help_text="Comma-separated list of recipient emails")
    sent_successfully = models.TextField(default="", help_text="Comma-separated list of successfully sent emails")
    # Assuming you want to keep track of which sends were successful

    def __str__(self):
        return f"Newsletter {self.subject} sent on {self.sent_date.strftime('%Y-%m-%d %H:%M:%S')}"

    def was_sent_successfully_to(self, email):
        return email in self.sent_successfully.split(',')

