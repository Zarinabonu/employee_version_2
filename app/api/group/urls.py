from django.urls import path

from app.api.group import views

urlpatterns = [
    path('create', views.GroupCreateAPIView.as_view(), name='api-group-create'),
    path('list', views.GroupListAPIView.as_view(), name='api-group-list'),
]
