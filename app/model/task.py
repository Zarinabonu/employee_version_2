from django.db import models

from app.model.employee import Employee
from app.model.project import Project
from app.model.status import Status


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    task = models.TextField(null=True, blank=True)
    done_date = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


class Task_status(models.Model):
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    editer = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)