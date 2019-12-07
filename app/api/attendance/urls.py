from django.urls import path

from app.api.attendance import views

urlpatterns = [
    path('create/', views.Attandance_createAPIView.as_view(), name='api-attendance-create'),

]