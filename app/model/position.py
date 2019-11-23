from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    degree = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name