from datetime import datetime

from django.contrib.auth.models import User
from rest_framework import serializers
from app.model import Group
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes

from app.api.employee.extra_serializers import Group_listSerializer
from app.api.p_status.serializers import PStatusSerializer
from app.api.project.extra_serializers import employee_group_listSerializer, task_listSerializer, group_listSerializer, \
    project_status_listSerializer
from app.model import Project, Project_status, Status, Employee, Employee_group


class ProjectSerializer(ModelSerializer):
    group = Group_listSerializer(read_only=True)
    group_id = serializers.IntegerField(write_only=True)
    # status = PStatusSerializer(read_only=True)
    status_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Project
        fields = ('group',
                  'group_id',
                  'title',
                  'description',
                  'deadline',
                  'status_id')

    def create(self, validated_data):
        statuss = validated_data.pop('status_id')
        s = Status.objects.get(id=statuss)

        pro = Project(**validated_data)
        # statuss = validated_data.pop('status_id')
        pro.save()
        pro_status = Project_status.objects.create(project=pro, status=s)


        return pro

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        request = self.context['request']
        u = User.objects.get(id=request.user.id)
        if u.employee.position.degree == 9:
            statuss = validated_data.pop('status_id')
            s = Status.objects.get(code=statuss)
            request = self.context['request']
            u = Employee.objects.get(id=request.user.id)

            pro_status = Project_status.objects.create(project=instance, status=s)
            pro_status.editer = u
            print('date is:',datetime.today().date(), 'print s :', s.code)

            if s.code == 4:
                instance.done_date = datetime.today().date()
                print(datetime.today().date())
                pro_status.save()
                instance.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)


        return instance


class ProjectListSerializer(ModelSerializer):
    group = serializers.SerializerMethodField()
    task_set = task_listSerializer(read_only=True, many=True)
    project_status_set = project_status_listSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = ('id',
                  'group',
                  'title',
                  'description',
                  'deadline',
                  'done_date',
                  'created',
                  'task_set',
                  'project_status_set')

    def get_group(self, obj):
        qs = Group.objects.filter(project=obj)
        return group_listSerializer(qs, many=True, context=self.context).data

    def to_representation(self, instance):
        project_status = super(ProjectListSerializer, self).to_representation(instance)
        if instance.done_date is None:
            project_status.pop('done_date')

        return project_status


# class ProjectListSerializer(ModelSerializer):
#     group = GroupSerializer(read_only=True)
#     employee_group_set = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Project
#         fields = ('id',
#                   'group',
#                   'title',
#                   'description',
#                   'deadline',
#                   'done_date',
#                   'created',
#                   'employee_group_set',
#                   )
#
#     def get_employee_group_set(self, obj):
#         qs = Employee_group.objects.filter(group__project=obj)
#         return Project_employee_group_listSerializer(qs, many=True, context=self.context).data


# class ProjectListSerializer(ModelSerializer):
#     task_set = Task
#     class Meta:
#         model = Project
#         fields = ('id',
#                   'title',
#                   'description',
#                   'deadline')



