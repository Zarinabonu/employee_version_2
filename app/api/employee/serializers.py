from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes

from app.api.group.serializers import GroupSerializer
from app.api.position.serializers import PositionSerialzer
from django.contrib.auth.models import User

from app.api.salary.serializers import EmployeeSalary
from app.api.user.serializers import UserSerializer
from app.model import Employee, Employee_group
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
    group = GroupSerializer(read_only=True)
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


# class EmployeeListSerializer(ModelSerializer):
#     user = UserSerializer(read_only=True)
#     position = PositionSerialzer(read_only=True)
#     employee_group_set = EmployeeGroupSerializer(read_only=True, many=True)
#     employee_salary_set = EmployeeSalary(read_only=True, many=True)
#     accountant_set = AccountantSerializer(read_only=True ,source='accountant_id')
#     project_set =
#     class Meta:
#         model = Employee
#         fields = ('id',
#                   'user',
#                   'position',
#                   'image',
#                   'phone',
#                   'address',
#                   'register_num',
#                   'gender')

