from django.db import models

from places.models.city import City
from places.models.establishment import Establishment


class Place(models.Model):
    VACANT = 'vacant'
    OCCUPIED = 'occupied'
    ON_HOLD = 'on_hold'
    UNKNOWN = 'unknown'

    STATUS_TYPES = (
        (VACANT, 'Vacant'),
        (OCCUPIED, 'Occupied'),
        (ON_HOLD, 'On Hold'),
        (UNKNOWN, 'Unknown'),
    )

    status = models.CharField(max_length=8, choices=STATUS_TYPES, default=UNKNOWN)
    room_number = models.CharField(max_length=5, blank=False, verbose_name='Room #')
    floor_number = models.CharField(max_length=2, blank=False, verbose_name='Floor #')
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, default='1')

    def __str__(self):
        return f'{self.id} - {self.status} - {self.establishment}'
