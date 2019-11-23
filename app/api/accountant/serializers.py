from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes

from app.api.employee.serializers import EmployeeSerializer
from app.model import Accountant, Employee


class AccountantSerializer(ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Accountant
        fields = ('employee',
                  'employee_id',
                  'date',
                  'sum')

    def create(self, validated_data):
        accountant = Accountant(**validated_data)
        request = self.context['request']
        u = Employee.objects.get(id=request.user.id)
        accountant.accounter = u
        accountant.save()

        return accountant

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        for attr,value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance


# class EmployeelistSerializer(ModelSerializer):
#     user = UserSerializer(read_only=True)
#     position = Position_listSerializer(read_only=True)
#     class Meta:
#         model = Employee
#         fields = ('id',
#                   'user',
#                   'gender',
#                   'position',
#                   'image',
#                   'phone',
#                   'address')
#
#
# class AccountantListSerializer(ModelSerializer):
#     employee = EmployeelistSerializer(read_only=True)
#     accounter = EmployeelistSerializer(read_only=True)
#
#     class Meta:
#         model = Accountant
#         fields = ('id',
#                   'employee',
#                   'date',
#                   'sum',
#                   'accounter')