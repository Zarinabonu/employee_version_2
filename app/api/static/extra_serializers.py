from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.api.user.serializers import UserSerializer
from app.model import Employee, Attendance, Accountant, Employee_salary, Project, Project_status


class attandance_listSerializer(ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('id',
                  'date_start',
                  'date_finish')


class user_listSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    attendance_set = attandance_listSerializer(read_only=True, many=True)

    class Meta:
        model = Employee
        fields = ('id',
                  'user',
                  'image',
                  'attendance_set')


class GiveMSerializer(ModelSerializer):
    accounter = UserSerializer(read_only=True)

    class Meta:
        model = Accountant
        fields = ('id',
                  'sum',
                  'date',
                  'accounter')


class accountant_listSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    accountant_set = GiveMSerializer(many=True, read_only=True, source='accounter_id')

    class Meta:
        model = Employee
        fields = ('id',
                  'user',
                  'image',
                  'accountant_set',
                  )


class salary_employee_listSerializer(ModelSerializer):
    class Meta:
        model = Employee_salary
        fields = ('id',
                  'sum',
                  'date')



class salary_listSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    employee_salary_set = salary_employee_listSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ('id',
                  'user',
                  'image',
                  'employee_salary_set',
                  )


class projectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ('id',
                  'title',
                  'description',
                  'deadline')





class ProjectSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    project_process = serializers.SerializerMethodField()
    done_project = serializers.SerializerMethodField()


    class Meta:
        model = Employee
        fields = ('id',
                  'user',
                  'project_process',
                  'done_project')

    def get_project_process(self, obj):
        qs = Project.objects.filter(group__employee_group__employee=obj).filter(project_status__status__code=2)
        return projectSerializer(qs, many=True, context=self.context).data

    def get_done_project(self, obj):
        qs = Project.objects.filter(group__employee_group__employee=obj).filter(project_status__status__code=4)
        return projectSerializer(qs, many=True, context=self.context).data

    # def get_project(self, obj):
    #     qs = Project.objects.filter(group__employee_group__employee_id=obj).filter(done=False)
    #     return projectSerializer(qs, many=True, context=self.context).data
    #
    # def get_doneproject(self, obj):
    #     qs = Project.objects.filter(group__employee_group__employee_id=obj).filter(done=True)
    #     return projectSerializer(qs, many=True, context=self.context).data