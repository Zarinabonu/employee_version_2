from rest_framework.generics import CreateAPIView
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView

from app.api.attendance.serializers import AttendanceSerializer
from app.model import Attendance, Employee
from datetime import datetime
from datetime import date


class IsManagerUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.employee.position.degree == 9)


class Attandance_createAPIView(APIView):
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all()
    permission_classes = [IsManagerUser]

    def post(self, request):
        q_code = request.POST.get('qr_code')
        e = Employee.objects.get(register_num=q_code)
        if e.attendance_set.filter(created=datetime.now().date()).count()>0:
            e_finish = e.attendance_set.get(created=datetime.now().date())
            e_finish.date_finish = datetime.now()
            e_finish.save()
        else:
            a = Attendance.objects.create(employee_id=e, date_start = datetime.now())
            # a.date_start = datetime.now()
            # a.save()

        print(e.attendance_set.filter(created=datetime.now().date()).count())
        #     pass
        return Response(status=200)
