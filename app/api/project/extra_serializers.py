from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.api.employee.extra_serializers import status_listSerializer
from app.api.user.serializers import UserSerializer
from app.model import Employee_group, Employee, Task_status, Task, Group, Project_status


class employee_listSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    # gender = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ('id',
                  'user',
                  'position',
                  'gender',
                  'image',
                  'phone',
                  'address',
                  )


class employee_group_listSerializer(ModelSerializer):
    employee = serializers.SerializerMethodField()

    class Meta:
        model = Employee_group
        fields = ('id',
                  'employee',
                  'name',
                  'created')

    def get_employee(self, obj):
        qs = Employee.objects.filter(employee_group=obj)
        return employee_listSerializer(qs, many=True, context=self.context).data


class group_listSerializer(ModelSerializer):
    creater = employee_listSerializer(read_only=True)
    employee_group = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ('id',
                  'created',
                  'creater',
                  'employee_group')

    def get_employee_group(self, obj):
        qs = Employee_group.objects.filter(group=obj)
        return employee_group_listSerializer(qs, many=True, context=self.context).data


class task_status_listSerializer(ModelSerializer):
    status = status_listSerializer(read_only=True)
    class Meta:
        model = Task_status
        fields = ('id',
                  'status',
                  'task',
                  'created',
                  'editer')


class task_listSerializer(ModelSerializer):
    task_status_set = task_status_listSerializer(read_only=True, many=True)
    employee = employee_listSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('id',
                  'task',
                  'employee',
                  'done_date',
                  'created',
                  'task_status_set')

    def to_representation(self, instance):
        task_status = super(task_listSerializer, self).to_representation(instance)

        if instance.done_date is None:
            task_status.pop('done_date')
        return task_status


class project_status_listSerializer(ModelSerializer):
    status = status_listSerializer(read_only=True)
    editer = employee_listSerializer(read_only=True)

    class Meta:
        model = Project_status
        fields = ('id',
                  'status',
                  'created',
                  'editer')


