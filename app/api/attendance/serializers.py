from rest_framework.serializers import ModelSerializer

from app.model import Attendance


class AttendanceSerializer(ModelSerializer):
    class Meta:
        model = Attendance
        fields = ()

