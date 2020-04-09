from django.db import models


class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name
