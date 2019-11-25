from rest_framework.serializers import ModelSerializer

from app.api.employee.extra_serializers import employee_listSerializer
from app.model import Task_status, Task


class task_status_listSerializer(ModelSerializer):
    class Meta:
        model = Task_status
        fields = ('id',
                  'status',
                  'created',
                  'editer')


class task_listSerializer(ModelSerializer):
    task_status_set = task_status_listSerializer(read_only=True, many=True)

    class Meta:
        model = Task
        fields = ('id',
                  'task',
                  'done_date',
                  'created',
                  'task_status_set')


class Project_task_listSerializer(ModelSerializer):
    task_status_set = task_status_listSerializer(read_only=True, many=True)
    employee = employee_listSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('id',
                  'employee',
                  'task',
                  'done_date',
                  'created',
                  'task_status_set')

