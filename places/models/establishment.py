from django.db import models

from places.models.city import City


class Establishment(models.Model):
    name = models.CharField(max_length=50, blank=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE, default='1')
    address = models.CharField(max_length=50, blank=False, default='N/A')
    phone = models.CharField(max_length=20, blank=False, default='N/A')
    email = models.CharField(max_length=30, blank=False, default='N/A')

    def __str__(self):
        return f'{self.name}'
