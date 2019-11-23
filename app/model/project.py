from django.db import models

from app.model.employee import Employee
from app.model.status import Status
from .group import Group


class Project(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    done_date = models.DateField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)


class Project_status (models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    created = models.DateField(auto_now_add=True)
    editer = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)