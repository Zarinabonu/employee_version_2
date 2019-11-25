from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from app.api.employee.extra_serializers import employee_listSerializer
from app.api.position.serializers import Position_listSerializer
from app.api.user.serializers import UserSerializer
from app.model import Group, Project, Task, Task_status, Employee


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
    creater = employee_listSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = ('id',
                  'name',
                  'created',
                  'creater')


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
