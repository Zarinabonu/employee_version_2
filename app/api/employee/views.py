from rest_framework import viewsets
from app.api.employee import serializers
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.views import APIView

from app.api.employee.serializers import EmployeeSerializer, EmployeeGroupSerializer, EmployeeListSerializer
from app.model import Employee, Employee_group

from rest_framework import filters


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


# class EmployeeListAPIView(ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeListSerializer
#
#     def get_queryset(self):
#         e = self.request.data.get('id')
#         employee = Employee.objects.get(id=e)

# class GroupViewSet(MultiSerializerViewSet)

class EmployeeListAPIView(ListAPIView):
    queryset = Employee.objects.all()

    def get_serializer_class(self):
        e = self.request.GET.get('employee_id')
        if e:
            return serializers.EmployeeListSerializer
        return serializers.EmployeList

    def get_queryset(self):
        e = self.request.GET.get('employee_id')
        employee_f_name = self.request.GET.get('employee_f_name')
        employee_l_name = self.request.GET.get('employee_l_name')
        employee_position = self.request.GET.get('employee_position')
        em = Employee.objects.all()
        if e:
            em = Employee.objects.filter(id=e)
        elif employee_f_name:
            em = Employee.objects.filter(user__first_name=employee_f_name)
        elif employee_l_name:
            em = Employee.objects.filter(user__last_name=employee_l_name)
        elif employee_position:
            em = Employee.objects.filter(user__last_name=employee_position)
        return em
