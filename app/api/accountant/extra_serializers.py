from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.api.user.serializers import UserSerializer
from app.model import Employee, Employee_salary


class employee_salary_listSerializer(ModelSerializer):
    class Meta:
        model = Employee_salary
        fields = ('id',
                  'sum',
                  'date',
                  'created')


class employee_listSerializer(ModelSerializer):
    employee_salary_set = employee_salary_listSerializer(read_only=True, many=True)
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
                  'employee_salary_set')

    # def get_gender(self, obj):
    #     return obj.gender
