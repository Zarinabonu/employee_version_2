from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.api.user.serializers import UserSerializer
from app.model import Employee_group, Employee_salary, Accountant, Employee, Attendance, Project, Project_status, \
    Status, Task, Task_status, Group


class employee_listSerializer(ModelSerializer):
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
                  )


class Group_listSerializer(ModelSerializer):
    creater = employee_listSerializer(read_only=True)

    class Meta:
        model = Group
        fields = ('id',
                  'name',
                  'created',
                  'creater')

class employee_group_listSerializer(ModelSerializer):
    group = Group_listSerializer(read_only=True)

    class Meta:
        model = Employee_group
        fields = ('id',
                  'group',
                  'name',
                  'created')


class employee_salary_listSerializer(ModelSerializer):
    class Meta:
        model = Employee_salary
        fields = ('id',
                  'sum',
                  'date',
                  'created')


class accountant_listSerializer(ModelSerializer):
    accounter = employee_listSerializer(read_only=True, source='accounter_id')

    class Meta:
        model = Accountant
        fields = ('id',
                  'sum',
                  'date',
                  'accounter')


class attendance_listSerializer(ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('id',
                  'date_start',
                  'date_finish',
                  'created')


class status_listSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = ('id',
                  'name',
                  'code')


class project_status_listSerializer(ModelSerializer):
    status = status_listSerializer(read_only=True)
    editer = employee_listSerializer(read_only=True)

    class Meta:
        model = Project_status
        fields = ('id',
                  'status',
                  'created',
                  'editer')


class project_listSerializer(ModelSerializer):
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
                  'project_status_set')

    def to_representation(self, instance):
        project_status = super(project_listSerializer, self).to_representation(instance)
        if instance.done_date is None:
            project_status.pop('done_date')

        return project_status



class task_status_listSerializer(ModelSerializer):
    status = status_listSerializer(read_only=True)
    class Meta:
        model = Task_status
        fields = ('id',
                  'status',
                  'task',
                  'created',
                  'editer')


class task_listSerializer(ModelSerializer):
    project = serializers.SerializerMethodField()
    task_status_set = task_status_listSerializer(read_only=True, many=True)

    class Meta:
        model = Task
        fields = ('id',
                  'project',
                  'task',
                  'done_date',
                  'created',
                  'task_status_set')

    def get_project(self, obj):
        qs = Project.objects.filter(task=obj)
        return project_listSerializer(qs,many=True, context=self.context).data

    def to_representation(self, instance):
        task_status = super(task_listSerializer, self).to_representation(instance)

        if instance.done_date is None:
            task_status.pop('done_date')
        return task_status

