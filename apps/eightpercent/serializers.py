from rest_framework.serializers import ModelSerializer, StringRelatedField

from apps.eightpercent.models import Account, Transaction


class WithdrawSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            "transaction_amount",
            "description",
        )


class ReadAccountSerializer(ModelSerializer):
    customer_name = StringRelatedField(source="customer")

    class Meta:
        model = Account
        fields = (
            "account_number",
            "balance",
            "customer_name",
        )
        read_only_fields = (
            "account_number",
            "balance",
            "customer_name",
        )
