from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

from app.api.task.serializers import TaskSerializer, ProjectSerializer, TaskListSerializer
from app.model import Task, Project


class TaskCreateAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateAPIView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_url_kwarg = 'id'


class TaskDestroyAPIView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_url_kwarg = 'id'


class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer

class ProjectListAPIView(ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()