from rest_framework.serializers import ModelSerializer

from app.api.employee.extra_serializers import employee_listSerializer
from app.model import Accountant


class accountant_listSerializer(ModelSerializer):
    accounter_id = employee_listSerializer(read_only=True)

    class Meta:
        model = Accountant
        fields = ('id',
                  'date',
                  'sum',
                  'accounter_id')