from django.conf import settings
from django.db import models
import base64

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="images/", blank=True)
    image_base64 = models.CharField(max_length=1000000, blank=True)
    available = models.BooleanField(null=False, default=False)

    def save(self, *args, **kwargs):
        self.image_base64 = base64.b64encode(self.image.read()).decode('utf-8')
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_base64 = models.CharField(max_length=1000000, blank=True)
    available = models.BooleanField(null=False, default=False)

    def __str__(self):
        return f"{self.name} - {self.user}"