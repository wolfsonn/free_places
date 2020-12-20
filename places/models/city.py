from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class City(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
