from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.model import Employee


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date_start = models.DateTimeField(null=True, blank=True)
    date_finish = models.DateTimeField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    check_out = models.BooleanField(default=True)


@receiver(post_save, sender=Attendance)
def create_check_out(sender, instance, created, **kwargs):
    if created:
        if instance.check_out:
            request = instance.employee_id
            att = Attendance.objects.filter(employee_id=request)
            att = att.exclude(date_start=instance.date_start)
            last_date = att.last().date_start.date()
            new_date = instance.date_start.date()
            subtitution = new_date - last_date
            for attandance in range(1, subtitution.days):
                at = Attendance.objects.create(employee_id=instance.employee_id, check_out=False)
                at.created = last_date+timedelta(days=attandance)
                at.save()
            print('DAYS', subtitution)



