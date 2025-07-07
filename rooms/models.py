from django.db import models

from django.db import models

ROOM_STATUS = [
    ('available', 'متاحة'),
    ('occupied', 'مشغولة'),
    ('cleaning', 'تحتاج تنظيف'),
    ('maintenance', 'قيد الصيانة'),
]

class Room(models.Model):
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=ROOM_STATUS, default='available')
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def str(self):
        return f'Room {self.number}'
