from django.contrib.auth import get_user_model
from django.db import models

from places.models.city import City

UserModel = get_user_model()


class Establishment(models.Model):
    name = models.CharField(max_length=50, blank=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=30, blank=False)
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'
