from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.api.employee.extra_serializers import status_listSerializer
from app.api.user.serializers import UserSerializer
from app.model import Employee, Employee_group, Group, Task_status, Project, Project_status


#
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


class project_listSerializer(ModelSerializer):
    project_set = project_status_listSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = ('title',
                  'description',
                  'deadline',
                  'done_date',
                  'created',
                  'project_set')

    def to_representation(self, instance):
        pro_status = super(project_listSerializer, self).to_representation(instance)

        if instance.done_date is None:
            pro_status.pop('done_date')
        return pro_status


class employee_group_listSerializer(ModelSerializer):
    employee = serializers.SerializerMethodField()
    project = serializers.SerializerMethodField()

    class Meta:
        model = Employee_group
        fields = ('id',
                  'employee',
                  'name',
                  'created',
                  'project')

    def get_employee(self, obj):
        qs = Employee.objects.filter(employee_group=obj)
        return employee_listSerializer(qs, many=True, context=self.context).data

    def get_project(self, obj):
        qs = Project.objects.filter(group__employee_group=obj)
        return project_listSerializer(qs, many=True, context=self.context).data


class group_listSerializer(ModelSerializer):
    creater = employee_listSerializer(read_only=True)
    employee_group = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ('id',
                  'name',
                  'employee_group',
                  'creater')

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

