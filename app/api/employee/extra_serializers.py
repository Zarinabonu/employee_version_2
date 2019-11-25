from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.api.position.serializers import Position_listSerializer
from app.api.task.extra_serializers import  Project_task_listSerializer
from app.api.user.serializers import UserSerializer
from app.model import Employee_group, Employee, Task


class employee_listSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    position = Position_listSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = ('id',
                  'user',
                  'position',
                  'image',
                  'phone')


class employee_group_listSerializer(ModelSerializer):
    # group = GroupListSerializer(read_only=True)

    class Meta:
        model = Employee_group
        fields = ('id',
                  'group',
                  'name',
                  'created')


class Project_employee_group_listSerializer(ModelSerializer):
    # group = GroupListSerializer(read_only=True)
    employee = employee_listSerializer(read_only=True)
    task_set = serializers.SerializerMethodField()

    class Meta:
        model = Employee_group
        fields = ('id',
                  'employee',
                  'group',
                  'name',
                  'created',
                  'task_set')

    def get_task_set(self, obj):
        qs = Task.objects.filter(project__group__employee_group=obj)
        return Project_task_listSerializer(qs, many=True, context=self.context).data