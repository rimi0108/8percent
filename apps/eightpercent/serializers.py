from rest_framework import serializers

from apps.eightpercent.models import Account, Transaction

class DepositSerializer(serializers.ModelSerializer):
    transaction_type = serializers.CharField(default="DEPOSIT")
    account_balance = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = (
            "account",
            "transaction_type", 
            "transaction_amount",
            "description",
            "account_balance",
        )
        read_only_fields = (
            "transaction_type",
            "transaction_date",
            "account_balance",
        )

    def get_account_balance(self, obj):
        account_balance = int(obj.account.balance + obj.transaction_amount)
        obj.account.balance = account_balance
        obj.account.save()
        return account_balance
    