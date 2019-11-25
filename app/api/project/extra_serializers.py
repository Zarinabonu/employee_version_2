from rest_framework.serializers import ModelSerializer

from app.api.task.extra_serializers import task_listSerializer
from app.model import Project, Project_status


class project_status_listSerializer(ModelSerializer):
    class Meta:
        model = Project_status
        fields = ('id',
                  'status',
                  'created',
                  'editer')



class project_listSerializer(ModelSerializer):
    project_status_set = project_status_listSerializer(read_only=True, many=True)
    task_set = task_listSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = ('id',
                  'title',
                  'description',
                  'deadline',
                  'created',
                  'done_date',
                  'project_status_set',
                  'task_set')

    def to_representation(self, instance):
        project_status = super(project_listSerializer, self).to_representation(instance)
        if instance.done_date is None:
            project_status.pop('done_date')

        return project_status

    # def to_task_set(self, instance):
    #     task_done = super(project_listSerializer, self).to_representation(instance)
    #     task = Task.objects.get(project=instance)
    #     print('TASK IS:', task)
    #     if task.done_date is None:
    #         task_done.pop('task_set')

        return task_done
