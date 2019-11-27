from rest_framework.serializers import ModelSerializer

from app.model import Status


class PStatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = ('name',
                  'code',)


class ProjectStatusListSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = ('id',
                  'name',
                  'code')