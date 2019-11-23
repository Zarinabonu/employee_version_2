from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    code = models.IntegerField(null=True, blank=True)
