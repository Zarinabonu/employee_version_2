
from django.urls import include, path

urlpatterns = [
    path('group/', include('app.api.group.urls')),
    path('employee/', include('app.api.employee.urls')),
    path('salary/', include('app.api.salary.urls')),
    path('accountant/', include('app.api.accountant.urls')),
    path('attendance/', include('app.api.attendance.urls')),
    path('project/', include('app.api.project.urls')),
    path('task/', include('app.api.task.urls')),

]