from rest_framework.serializers import ModelSerializer

from apps.eightpercent.models import Transaction


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            "transaction_type",
            "transaction_amount",
            "transaction_date",
            "description",
            "account",
        )
