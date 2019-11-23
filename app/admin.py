from django.contrib import admin

from .model import Employee_group, Employee_salary, Employee,Group, Position, Project_status, Project, Status, Task_status, Task, Accountant, Attendance
admin.site.register(Employee_group)
admin.site.register(Employee_salary)
admin.site.register(Employee)
admin.site.register(Group)
admin.site.register(Position)
admin.site.register(Project_status)
admin.site.register(Project)
admin.site.register(Status)
admin.site.register(Task_status)
admin.site.register(Task)
admin.site.register(Accountant)
admin.site.register(Attendance)
# Register your models here.
