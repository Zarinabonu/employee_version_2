from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

from app.api.employee.serializers import EmployeeSerializer, EmployeeGroupSerializer, EmployeeListSerializer
from app.model import Employee, Employee_group


class EmployeeCreateAPIView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeUpdateAPIView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_url_kwarg = 'id'

class EmployeeDestroyAPIView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_url_kwarg = 'id'


class EmployeeGroupCreateAPIView(CreateAPIView):
    queryset = Employee_group.objects.all()
    serializer_class = EmployeeGroupSerializer


class EmployeeGroupUpdateAPIView(UpdateAPIView):
    queryset = Employee_group.objects.all()
    serializer_class = EmployeeGroupSerializer
    lookup_url_kwarg = 'id'


class EmployeeGroupDestroyAPIView(DestroyAPIView):
    queryset = Employee_group.objects.all()
    serializer_class = EmployeeGroupSerializer
    lookup_url_kwarg = 'id'


class EmployeeListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeListSerializer