from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes

from app.model import Employee_salary


class EmployeeSalary(ModelSerializer):
    # employee = EmployeeSerializer(read_only=True, many=True)
    employee_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Employee_salary
        fields = ('employee_id',
                  'sum',
                  'date')

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        for attr,value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance