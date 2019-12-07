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

    def get_queryset(self):
        id_pro = self.request.GET.get('project_id')
        title_pro = self.request.GET.get('project_title')
        project = Project.objects.all()
        if id_pro:
            project = project.filter(id=id_pro)
        elif title_pro:
            project = project.filter(title=title_pro)