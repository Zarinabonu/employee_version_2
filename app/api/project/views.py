from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

from app.api.project.serializers import ProjectSerializer, ProjectListSerializer
from app.model import Project


class ProjectCreateAPIView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectUpdateAPIView(UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_url_kwarg = 'id'


class ProjectDestroyAPIView(DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_url_kwarg = 'id'


class ProjectListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer