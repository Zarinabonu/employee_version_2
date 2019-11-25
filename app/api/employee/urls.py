from django.urls import path
from app.api.employee import views

urlpatterns = [
    path('create', views.EmployeeCreateAPIView.as_view(), name='api-employee-create'),
    path('update/<int:id>', views.EmployeeUpdateAPIView.as_view(), name='api-employee-update'),
    path('destroy/<int:id>', views.EmployeeDestroyAPIView.as_view(), name='api-employee-destroy'),
    path('group/create', views.EmployeeGroupCreateAPIView.as_view(), name='api-employee-group-create'),
    path('group/update/<int:id>', views.EmployeeGroupUpdateAPIView.as_view(), name='api-employee-group-update'),
    path('group/destroy/<int:id>', views.EmployeeGroupDestroyAPIView.as_view(), name='api-employee-group-destroy'),
    path('list', views.EmployeeListAPIView.as_view(), name='api-employee-list'),
]