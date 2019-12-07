from datetime import datetime, timedelta

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from app.api.static.extra_serializers import attandance_listSerializer
from app.api.static.serializers import StaticSerializer
from app.model import Employee, Attendance


class Static_listAPIView(ListAPIView):
    serializer_class = attandance_listSerializer
    queryset = Attendance.objects.all()

    def get_queryset(self):
        N=6
        queryset = Attendance.objects.all()
        e = self.request.GET.get('employee_id')
    #     # em = Employee.objects.filter(id=e)
        queryset = Attendance.objects.filter(employee__id=e)
    #     queryset = queryset.filter(created__week_day__gte=1)
    #     # attandance = q.filter(date_start__day=)
    #     date_N_days_ago = datetime.now() - timedelta(days=N)
    #     # queryset = queryset.filter(date_start__gte=date_N_days_ago)
    #     queryset = queryset.order_by('created')[:6]
    #     print('R',queryset)
    #
    #     print('Q', date_N_days_ago)
    # #
        return queryset


class Employee_ListAPIView(APIView):
    def get(self, request):
        list = []
        list.append(request.user)
        serializer = StaticSerializer(list, many=False)
        serializer.context['request'] = request
        return Response(serializer.data)

