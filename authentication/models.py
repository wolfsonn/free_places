from django.contrib.auth.models import User
from django.db import models

from places.models.establishment import Establishment


class UserProfile(models.Model):
    profile_picture = models.ImageField(
        upload_to='users',
        blank=True
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    establishment = models.ForeignKey(Establishment, on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return self.user.username
