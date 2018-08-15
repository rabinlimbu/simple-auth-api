from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address1 = models.CharField('Address Line 1', max_length=200, blank=True, null=True)
    address2 = models.CharField('Address Line 2', max_length=50, blank=True, null=True,
                                help_text="Apt# or Unit# or Ct/House#")
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.TextField(max_length=100, blank=True, null=True)
    address_type = models.CharField(max_length=100, blank=True, null=True, help_text="Shipping or Billing")
    date_entered = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
