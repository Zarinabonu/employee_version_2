from django.db import models

from app.model import Employee


class Accountant(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_id')
    date = models.DateField()
    sum = models.IntegerField()
    accounter = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='accounter_id')
