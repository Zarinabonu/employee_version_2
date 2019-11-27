from datetime import datetime

from django.contrib.auth.models import User
from rest_framework import serializers
from app.model import Group
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes

from app.api.employee.serializers import EmployeeSerializer
from app.api.p_status.serializers import PStatusSerializer
from app.api.project.serializers import ProjectSerializer
from app.api.task.extra_serializers import group_listSerializer, task_status_listSerializer
from app.model import Task, Status, Task_status, Employee, Project


class TaskSerializer(ModelSerializer):
    project = ProjectSerializer(read_only=True)
    project_id = serializers.IntegerField(write_only=True)
    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.IntegerField(write_only=True)
    status = serializers.IntegerField(write_only=True)

    class Meta:
        model = Task
        fields = ('project',
                  'project_id',
                  'employee',
                  'employee_id',
                  'task',
                  'status')

    def create(self, validated_data):
        sta = validated_data.pop('status')
        taskk = Task(**validated_data)
        taskk.save()
        statuss = Status.objects.get(code=sta)
        t = Task_status.objects.create(status=statuss, task=taskk)

        return taskk

    def update(self, instance, validated_data):
         raise_errors_on_nested_writes('update', self, validated_data)
         request = self.context['request']
         u = User.objects.get(id=request.user.id)
         if u.employee.position.degree == 9:
             status_code = validated_data.pop('status')
             task = Task(**validated_data)
             task.save()

             employee_id = Employee.objects.get(id=request.user.id)

             status = Status.objects.get(code=status_code)
             t = Task_status.objects.create(status=status, task=task)
             t.editer = employee_id

             if status.code == 4:
                 instance.done_date = datetime.today().date()
                 print(datetime.today().date())
                 t.save()
                 instance.save()

         for attr, value in validated_data.items():
             setattr(instance, attr, value)

         return instance


class TaskListSerializer(ModelSerializer):
    # group = serializers.SerializerMethodField()
    group_set = serializers.SerializerMethodField()
    task_status_set = task_status_listSerializer(read_only=True, many=True)

    class Meta:
        model = Task
        fields = ('id',
                  'group_set',
                  'task',
                  'done_date',
                  'task_status_set',
                  'created')

    def get_group_set(self, obj):
        qs = Group.objects.filter(project__task=obj)
        return group_listSerializer(qs, many=True, context=self.context).data

    def to_representation(self, instance):
        task_status = super(TaskListSerializer, self).to_representation(instance)

        if instance.done_date is None:
            task_status.pop('done_date')
        return task_status


# class TaskStatusSerializer(ModelSerializer):
#     status = PStatusSerializer(read_only=True)
#     class Meta:
#         model = Task_status
#         fields = ('id',
#                   'status',
#                   )
#
#
# class ProjectSerializer(ModelSerializer):
#     class Meta:
#         model = Project
#         fields = ('id',
#                   'title',
#                   'description',
#                   )
#
#
# class TaskListSerializer(ModelSerializer):
#     task_status_set = TaskStatusSerializer(read_only=True, many=True)
#     employee = EmployeeSerializer(read_only=True)
#     project = ProjectSerializer(read_only=True)
#
#     class Meta:
#         model = Task
#         fields = ('id',
#                   'project',
#                   'task',
#                   'employee',
#                   'task_status_set')

