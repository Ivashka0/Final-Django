from django.conf import settings
from django.db import models

# Create your models here.


class CreditCard(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=500000)
    sum = models.DecimalField(max_digits=1000, decimal_places=2)
    credit_number = models.CharField(max_length=500000)
    expiration = models.CharField(max_length=10000)
    security_code = models.IntegerField()
    status = models.CharField(max_length=10000, choices=(('Sent', 'Sent'), ('Processing', 'Processing'),
                                                         ('Canceled', 'Canceled')), default='Processing')

    def __str__(self):
        return f"{self.name} - {self.id}"