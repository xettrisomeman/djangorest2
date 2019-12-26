from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass



class Address(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)


    def __str__(self):
        return self.city


class Person(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    first_name = models.CharField( max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    
    