from datetime import datetime, timedelta

from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView

from apps.eightpercent.models import Transaction
from apps.eightpercent.serializers import TransactionSerializer


class TransactionView(ListAPIView):
    """User Transaction View"""
    permission_classes = [AllowAny]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def filter_queryset(self, queryset):

        account_number = self.request.user.account

        # get query params
        transaction_type = self.request.query_params.get("transaction_type")
        start_day = self.request.query_params.get("start_day")
        # add one day to end_day
        end_day = self.request.query_params.get("end_day")
        strp_end_day = datetime.strptime(end_day, "%Y-%m-%d")
        modified_day = strp_end_day + timedelta(days=1)
        end_day = datetime.strftime(modified_day, "%Y-%m-%d")
        ordering = self.request.query_params.get("ordering")

        filter_kwargs = {"account": account_number}

        if (transaction_type == 'DEPOSIT') or (transaction_type == 'WITHDRAW'):
            filter_kwargs['transaction_type'] = transaction_type

        if (start_day is not None) and (end_day is not None):
            filter_kwargs['transaction_date__gte'] = start_day
            filter_kwargs['transaction_date__lte'] = end_day

        queryset = queryset.filter(**filter_kwargs)

        if (ordering == 'True') or (ordering == 'true'):
            queryset = queryset.order_by("-transaction_date")

        return super().filter_queryset(queryset)
