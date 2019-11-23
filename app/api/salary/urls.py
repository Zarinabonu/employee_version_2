from django.urls import path

from app.api.salary import views

urlpatterns = [
    path('create', views.EmployeeSalaryCreateAPIView.as_view(), name='api-employee-salary-create'),
    path('update/<int:id>', views.EmployeeSalaryUpdateAPIView.as_view(), name='api-employee-salary-update'),
    path('destroy/<int:id>', views.EmployeeSalaryDestroyAPIView.as_view(), name='api-employee-salary-destroy'),
]