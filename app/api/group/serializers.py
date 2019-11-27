from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.api.group.extra_serializers import employee_listSerializer, employee_group_listSerializer
from app.model import Group, Project, Task, Task_status, Employee, Employee_group


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',
                  )

    def create(self, validated_data):
        group = Group(**validated_data)
        g = self.context['request']
        u = User.objects.get(id=g.user.id)
        group.creater = u
        group.save()

        return group


class GroupListSerializer(ModelSerializer):
    creater = employee_listSerializer(read_only=True)
    employee_group_set = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ('id',
                  'name',
                  'created',
                  'creater',
                  'employee_group_set')

    def get_employee_group_set(self, obj):
        qs = Employee_group.objects.filter(group=obj)
        return employee_group_listSerializer(qs, many=True, context=self.context).data





# class GroupListSerializer(ModelSerializer):
#     creater = employee_listSerializer(read_only=True, many=True)
#
#     class Meta:
#         model = Group
#         fields = ('id',
#                   'name',
#                   'created',
#                   'creater')


# class TaskStatusSerializer(ModelSerializer):
#     class Meta:
#         model = Task_status
#         fields = ('id',
#                   'status',
#                   'editer',
#                   'created')
#
#
# class TaskForProjectSerializer(ModelSerializer):
#     task_status_set = TaskStatusSerializer(many=True, read_only=True)
#     class Meta:
#         model = Task
#         fields = ('id',
#                   'employee_id',
#                   'task',
#                   'done_date',
#                   'created',
#                   'task_status_set')
#
#
# class ProjectForGroupSerializer(ModelSerializer):
#     task_set = TaskForProjectSerializer(many=True, read_only=True)
#     class Meta:
#         model = Project
#         fields = ('id',
#                   'title',
#                   'description',
#                   'deadline',
#                   'done_date',
#                   'created',
#                   'task_set')
#
#
# class GroupListSerializer(ModelSerializer):
#     project_set = ProjectForGroupSerializer(many=True, read_only=True)
#     class Meta:
#         model = Group
#         fields = ('id',
#                   'name',
#                   'creater',
#                   'project_set',
#                   )
