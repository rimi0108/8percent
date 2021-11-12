from rest_framework import serializers

from apps.eightpercent.models import Transaction

# class CurrentUserDefault:
#     requires_context = True

#     def __call__(self, serializer_field):
#         return serializer_field.context['request'].user

#     def __repr__(self):
#         return '%s()' % self.__class__.__name__


class DepositSerializer(serializers.ModelSerializer):
    # account = serializers.HiddenField(default=serializers.CurrentUserDefault())
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
