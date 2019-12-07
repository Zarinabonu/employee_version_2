from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes

from app.api.employee.extra_serializers import employee_group_listSerializer, \
    accountant_listSerializer, employee_salary_listSerializer, employee_listSerializer, attendance_listSerializer, \
    project_listSerializer, task_listSerializer
from app.api.employee.extra_serializers import Group_listSerializer
from app.api.group.serializers import GroupSerializer
from app.api.position.serializers import PositionSerialzer
from django.contrib.auth.models import User

from app.api.user.serializers import UserSerializer
from app.model import Employee, Employee_group, Employee_salary, Accountant, Attendance, Project, Project_status, Task, \
    Task_status
from rest_framework.authtoken.models import Token


class EmployeeSerializer(ModelSerializer):
    position = PositionSerialzer(read_only=True)
    position_id = serializers.IntegerField(write_only=True)
    username = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    is_active = serializers.BooleanField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'is_active',
                  'password',
                  'image',
                  'phone',
                  'address',
                  'position',
                  'gender',
                  'position_id',
                  )

    def create(self, validated_data):
        username = validated_data.pop('username')
        #     _id = serializers.IntegerField(write_only=True)
        firstname = validated_data.pop('first_name')
        lastname = validated_data.pop('last_name')
        email = validated_data.pop('email')
        is_active = validated_data.pop('is_active')
        password = validated_data.pop('password')

        employee = Employee(**validated_data)
        u = User.objects.create(username=username, first_name=firstname, last_name=lastname, email=email,
                                is_active=is_active)
        u.set_password(password)
        u.save()
        employee.user = u
        employee.save()
        token = Token.objects.create(user=u)
        token.save()

        return employee

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        if validated_data.get('password'):
            p = validated_data.pop('password')
            instance.user.set_password(p)
        for attr, value in validated_data.items():
            setattr(instance.user, attr, value)
            setattr(instance, attr, value)

        instance.user.save()
        instance.save()

        return instance


class EmployeeGroupSerializer(ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.IntegerField(write_only=True)
    group = Group_listSerializer(read_only=True)
    group_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Employee_group
        fields = ('employee',
                  'employee_id',
                  'group',
                  'group_id',
                  'name')

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        for attr,value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance


class EmployeList(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id',
                  'user',
                  'image',
                  'phone',
                  'address',
                  'position',
                  'gender',
                  )


class EmployeeListSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    employee_group_set = employee_group_listSerializer(read_only=True, many=True)
    employee_salary_set = employee_salary_listSerializer(read_only=True, many=True)
    accountant_set = accountant_listSerializer(read_only=True, source='accounter_id', many=True)
    attendance_set = attendance_listSerializer(read_only=True, many=True)
    project_set = serializers.SerializerMethodField()
    task_set = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ('id',
                  'user',
                  'image',
                  'phone',
                  'address',
                  'position',
                  'gender',
                  'register_num',
                  'employee_group_set',
                  'employee_salary_set',
                  'accountant_set',
                  'attendance_set',
                  'project_set',
                  'task_set')

    def get_project_set(self, obj):
        qs = Project.objects.filter(group__employee_group__employee=obj)
        return project_listSerializer(qs, many=True, context=self.context).data

    def get_task_set(self, obj):
        qs = Task.objects.filter(project__group__employee_group__employee=obj)
        return task_listSerializer(qs, many=True, context=self.context).data

    # def get_project_set(self, obj):
    #     qs = Project.objects.filter(group_id__employee_group__employee_id=obj)
    #     return project_listSerializer(qs, many=True, context=self.context).data

    def to_representation(self, instance):
        employee_status = super(EmployeeListSerializer, self).to_representation(instance)
        print('111', instance.position.degree)
        if self.context['request'].user.employee.position.degree == 9:
            employee_status.pop('employee_salary_set')
            employee_status.pop('accountant_set')
        elif self.context['request'].user.employee.position.degree == 8:
            employee_status.pop('employee_salary_set')
            employee_status.pop('accountant_set')

        elif self.context['request'].user.employee.position.degree == 7:
            employee_status.pop('employee_group_set')
        elif self.context['request'].user.employee.position.degree == 6:
            employee_status.pop('position')
            employee_status.pop('register_num')
            employee_status.pop('employee_group_set')
            employee_status.pop('employee_salary_set')
            employee_status.pop('accountant_set')
            employee_status.pop('attendance_set')
            employee_status.pop('project_set')
            employee_status.pop('task_set')

        return employee_status

