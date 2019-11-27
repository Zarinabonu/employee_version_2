from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.api.employee.extra_serializers import status_listSerializer
from app.api.user.serializers import UserSerializer
from app.model import Employee, Group, Employee_group, Project, Project_status, Task_status, Task


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


class project_status_listSerializer(ModelSerializer):
    status = status_listSerializer(read_only=True)
    editer = employee_listSerializer(read_only=True)

    class Meta:
        model = Project_status
        fields = ('id',
                  'status',
                  'created',
                  'editer')


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


class project_listSerializer(ModelSerializer):
    project_status_set = project_status_listSerializer(read_only=True, many=True)
    task = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ('id',
                  'group',
                  'title',
                  'description',
                  'deadline',
                  'done_date',
                  'created',
                  'project_status_set',
                  'task')

    def get_task(self, obj):
        qs = Task.objects.filter(project=obj)
        return task_listSerializer(qs, many=True, context=self.context).data

    def to_representation(self, instance):
        project_status = super(project_listSerializer, self).to_representation(instance)
        if instance.done_date is None:
            project_status.pop('done_date')

        return project_status

class employee_group_listSerializer(ModelSerializer):
    employee = serializers.SerializerMethodField()
    project = serializers.SerializerMethodField()

    class Meta:
        model = Employee_group
        fields = ('id',
                  'name',
                  'employee',
                  'created',
                  'project',
                  )

    def get_employee(self, obj):
        qs = Employee.objects.filter(employee_group=obj)
        return employee_listSerializer(qs, many=True, context=self.context).data

    def get_project(self, obj):
        qs = Project.objects.filter(group__employee_group=obj)
        return project_listSerializer(qs, many=True, context=self.context).data