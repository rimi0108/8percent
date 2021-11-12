import uuid

from django.conf import settings
from django.db import models


class Account(models.Model):

    account_number = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    balance = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    customer = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    class Meta:
        db_table = "accounts"


class Transaction(models.Model):

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, db_index=True
    )
    TransactionTypes = models.TextChoices("TransactionTypes", "WITHDRAW DEPOSIT")
    transaction_type = models.CharField(max_length=8, choices=TransactionTypes.choices)
    transaction_amount = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    transaction_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=20)
    account = models.ForeignKey("Account", on_delete=models.PROTECT)

    class Meta:
        db_table = "transactions"
