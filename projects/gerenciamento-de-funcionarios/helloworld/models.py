from django.db import models


class Employee(models.Model):
    name = models.CharField(
        max_length=255
    )
    last_name = models.CharField(
        max_length=255
    )
    cpf = models.CharField(
        max_length=255
    )
    time = models.IntegerField(
        default=0
    )
    salary = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    objects = models.Manager()
