from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from apps.eightpercent.models import Transaction
from apps.eightpercent.serializers import DepositSerializer


class DepositViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Transaction.objects.all()
    serializer_class = DepositSerializer
    permission_classes = [IsAuthenticated]
