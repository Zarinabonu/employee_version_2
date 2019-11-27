from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes

from app.api.accountant.extra_serializers import employee_listSerializer
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


class AccountantListAPIView(ModelSerializer):
    employee = employee_listSerializer(read_only=True)
    accounter = employee_listSerializer(read_only=True, source='accounter_id')

    class Meta:
        model = Accountant
        fields = ('id',
                  'employee',
                  'date',
                  'sum',
                  'accounter')

# class AccountantListSerializer(ModelSerializer):
#     employee = employee_listSerializer(read_only=True)
#     accounter = employee_listSerializer(read_only=True)
#
#     class Meta:
#         model = Accountant
#         fields = ('id',
#                   'employee',
#                   'date',
#                   'sum',
#                   'accounter')
#
