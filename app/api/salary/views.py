from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView

from app.api.salary.serializers import EmployeeSalary
from app.model import Employee_salary


class EmployeeSalaryCreateAPIView(CreateAPIView):
    queryset = Employee_salary.objects.all()
    serializer_class = EmployeeSalary


class EmployeeSalaryUpdateAPIView(UpdateAPIView):
    queryset = Employee_salary.objects.all()
    serializer_class = EmployeeSalary
    lookup_url_kwarg = 'id'

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class EmployeeSalaryDestroyAPIView(DestroyAPIView):
    queryset = Employee_salary.objects.all()
    serializer_class = EmployeeSalary
    lookup_url_kwarg = 'id'