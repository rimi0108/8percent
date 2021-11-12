from django.contrib import admin

from apps.eightpercent.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """Accont Model Admin"""

    list_display = (
        "account_number",
        "balance",
        "customer",
    )
