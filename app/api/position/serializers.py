from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
from django.contrib.auth.models import User
from app.model import Position
from rest_framework import serializers


class PositionSerialzer(ModelSerializer):
    class Meta:
        model = Position
        fields = ('name',
                  'degree')

    def create(self, validated_data):
        status = Position(**validated_data)
        request = self.context['request']
        if status.name == 'Director':
            status.degree = '5'
        elif status.name == 'Project meneger':
            status.degree = '4'
        elif status.name == 'Programmer':
            status.degree = '3'
        else:
            status.degree = '0'
        status.save()
        return status


class Position_listSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = ('id',
                  'name',
                  'degree')