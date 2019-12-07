from django.urls import path

from app.api.static import views
from app.api.static.views import Static_listAPIView

urlpatterns = [
    path('list', views.Static_listAPIView.as_view(), name='api-static-list'),
    path('e/list', views.Employee_ListAPIView.as_view(), name='api-static-e-list'),
]