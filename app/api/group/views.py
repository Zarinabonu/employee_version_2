from rest_framework.generics import CreateAPIView, ListAPIView

from app.api.group.serializers import GroupSerializer, GroupListSerializer
from app.model import Group


class GroupCreateAPIView(CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupListAPIView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupListSerializer