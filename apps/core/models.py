from django.db import models


class Car(models.Model):
    price = models.DecimalField(max_digits=15, decimal_places=2)
    mark = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year_manufactured = models.IntegerField()
    mileage = models.IntegerField()

    def __str__(self):
        return f'<Car [{self.id} - {self.mark}]>'
