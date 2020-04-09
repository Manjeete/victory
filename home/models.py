from django.db import models

class CustomerInfo(models.Model):
    day = models.CharField(max_length=20)
    time = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    no_of_person = models.CharField(max_length=10)
    def __str__(self):
        return self.name
