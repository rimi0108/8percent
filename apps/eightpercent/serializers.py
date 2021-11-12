from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    StringRelatedField,
    ValidationError,
)

from apps.eightpercent.models import Account, Transaction


class WithdrawSerializer(ModelSerializer):
    remaining_balance = SerializerMethodField()

    class Meta:
        model = Transaction
        fields = (
            "transaction_type",
            "transaction_amount",
            "description",
            "account",
            "remaining_balance",
        )
        read_only_fields = ("transaction_type", "account", "remaining_balance")

    def get_remaining_balance(self, obj):
        # return round(obj.account.balance - obj.transaction_amount)
        return int(obj.account.balance)

    def validate(self, attrs):
        account_number = self.context.get("request").user.account
        amount = attrs.get("transaction_amount")
        if amount < 0:
            raise ValidationError("Amount cannot be negative value.")
        if amount > account_number.balance:
            raise ValidationError("Balance is not enough.")
        account_number.balance = account_number.balance - amount
        account_number.save()
        return attrs


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
