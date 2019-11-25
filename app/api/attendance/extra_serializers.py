from rest_framework.serializers import ModelSerializer

from app.model import Attendance


class attendence_listSerializer(ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('id',
                  'date_start',
                  'date_finish',
                  'created')
