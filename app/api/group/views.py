from rest_framework.generics import CreateAPIView, ListAPIView

from app.api.group.serializers import GroupSerializer, GroupListSerializer
from app.model import Group


class GroupCreateAPIView(CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupListAPIView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupListSerializer

    def get_queryset(self):
        id_g = self.request.GET.get('group_id')
        name_g = self.request.GET.get('group_name')
        group = Group.objects.all()
        if id_g:
            group = group.filter(id=id_g)
        elif name_g:
            group = group.filter(name=name_g)
