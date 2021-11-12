from django.contrib import admin

from apps.eightpercent.models import Account, Transaction


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """Accont Model Admin"""

    list_display = (
        "account_number",
        "balance",
        "customer",
    )


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    """Transaction Model Admin"""

    list_display = (
        "transaction_type",
        "transaction_amount",
        "transaction_date",
        "description",
        "account",
    )
