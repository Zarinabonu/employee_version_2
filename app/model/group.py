from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    creater = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name or 'asd'