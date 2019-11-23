# from django.core.files import File
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from .position import Position
from .group import Group
from datetime import datetime
# import pyqrcode as pyqrcode


GENDER = (
    (0, _('Male')),
    (1, _('Female')),
)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    register_num = models.TextField(null=True, blank=True)
    gender = models.IntegerField(choices=GENDER)
    qr_file = models.FileField(null=True, upload_to="files/")
    status = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)


class Employee_group(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, default=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.employee.user.username or 'asd'

#
class Employee_salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    sum = models.IntegerField()
    date = models.DateField()
    created = models.DateField(auto_now_add=True)
#
id = 1
@receiver(post_save, sender=Employee)
def create_doctor_user(sender, instance, created, **kwargs):
    global id
    r5 = 0
    if created:
        currentYear = datetime.now().year
        r1 = str(currentYear % 10)
        r2 = str(datetime.now().month)
        if len(r2) == 1:
            r2 = "0" + r2
        r3 = str(chr(65 + datetime.today().weekday()))
        r4 = str(datetime.now().day)
        if len(r4) == 1:
            r4 = "0" + r4
        r5 = str(id)

        if len(r5) == 1:
            r5 = "00" + r5
        elif len(r5) == 2:
            r5 = "0" + r5
        print(instance)
        if instance.gender==1:
            r6 = str('W')
        else:
            r6 = 'M'
        print('WW', r1, r2, r3, r4, r5, r6)
        instance.register_num = r1 + r2 + r3 + r4 + r5 + r6
        somesjon = '{"register": ' + instance.register_num + '}'
        # quar = pyqrcode.create(somesjon)
        # quar.svg('qr_code.svg', scale=8)
        # local_file = open('qr_code.svg')
        # djangofile = File(local_file)
        # instance.qr_file.save('qr_img' + str(instance.id), djangofile)
        # local_file.close()

        instance.save()

        id += 1
