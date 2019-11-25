from rest_framework.serializers import ModelSerializer

from app.model import Employee_salary


class employee_salary_listSerializer(ModelSerializer):
    class Meta:
        model = Employee_salary
        fields = ('id',
                  'sum',
                  'date',
                  'created')
