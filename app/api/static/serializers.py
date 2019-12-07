from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from app.api.static.extra_serializers import user_listSerializer, accountant_listSerializer, salary_listSerializer, \
    ProjectSerializer
from app.model import Employee


class StaticSerializer(Serializer):
    attan = serializers.SerializerMethodField()
    accountant = serializers.SerializerMethodField()
    salary = serializers.SerializerMethodField()
    active_project = serializers.SerializerMethodField()

    def get_attan(self, obj):
        qs = Employee.objects.all()
        return user_listSerializer(qs, many=True, context=self.context).data

    def get_accountant(self, obj):
        qs = Employee.objects.all()
        print('hello:', qs)
        return accountant_listSerializer(qs, many=True, context=self.context).data

    def get_salary(self, obj):
        qs = Employee.objects.all()
        return salary_listSerializer(qs, many=True, context=self.context).data

    def get_active_project(self, obj):
        qs = Employee.objects.all()
        return ProjectSerializer(qs, many=True, context=self.context).data