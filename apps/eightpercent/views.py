from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from apps.eightpercent.models import Transaction
from apps.eightpercent.serializers import DepositSerializer

class DepositViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Transaction.objects.all()
    serializer_class = DepositSerializer
    permission_classes = [AllowAny]