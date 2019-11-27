from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import BasePermission

# from app.api.accountant.serializers import AccountantSerializer
from app.api.accountant.serializers import AccountantSerializer, AccountantListAPIView
from app.model import Accountant


class IsAccountantUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.employee.position.degree == 7)


class AccountantCreateAPIView(CreateAPIView):
    queryset = Accountant.objects.all()
    serializer_class = AccountantSerializer
    permission_classes = [IsAccountantUser]
#
#
class AccountantUpdateAPIView(UpdateAPIView):
    queryset = Accountant.objects.all()
    serializer_class = AccountantSerializer
    lookup_url_kwarg = 'id'
    permission_classes = [IsAccountantUser]


class AccountantDestroyAPIView(DestroyAPIView):
    queryset = Accountant.objects.all()
    serializer_class = AccountantSerializer
    lookup_url_kwarg = 'id'
    permission_classes = [IsAccountantUser]


class AccountantListAPIView(ListAPIView):
    queryset = Accountant.objects.all()
    serializer_class = AccountantListAPIView

    def get_queryset(self):
        qs = Accountant.objects.all()
        if self.request.GET.get('month'):
            qs = qs.filter(date__month=self.request.GET.get('month'))
        if self.request.GET.get('employee_id'):
            qs = qs.filter(employee_id=self.request.GET.get('employee_id'))

        return qs

