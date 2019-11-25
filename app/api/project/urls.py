from django.urls import path

from app.api.project import views

urlpatterns = [
    path('create', views.ProjectCreateAPIView.as_view(), name='api-project-create'),
    path('update/<int:id>', views.ProjectUpdateAPIView.as_view(), name='api-project-update'),
    path('destroy/<int:id>', views.ProjectDestroyAPIView.as_view(), name='api-project-destroy'),
    path('list', views.ProjectListAPIView.as_view(), name='api-project-list'),

]