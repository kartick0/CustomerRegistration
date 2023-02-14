from django.db import models

# Create your models here.
class CustomerRegistration(models.Model):
    cname=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    phoneNumber=models.CharField(max_length=200, blank=True)
    email=models.EmailField(max_length=200)
    
    REQUIRED_FIELDS = ['cname','age','address','email']