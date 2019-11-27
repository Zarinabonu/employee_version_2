from django.urls import path

from app.api.task import views

urlpatterns = [
    path('create', views.TaskCreateAPIView.as_view(), name='api-task-create'),
    path('update/<int:id>', views.TaskUpdateAPIView.as_view(), name='api-task-update'),
    path('destroy/<int:id>', views.TaskDestroyAPIView.as_view(), name='api-task-destroy'),
    path('project/list', views.ProjectListAPIView.as_view(), name='api-task-list'),
    path('list', views.TaskListAPIView.as_view(), name='api-task-list'),


]