from django.urls import path

from apps.eightpercent.views import (
    AccountView,
    DepositViewSet,
    TransactionView,
    WithdrawView,
)

app_name = "eightpercent"

urlpatterns = [
    path("account/", AccountView.as_view()),
    path("transactions", TransactionView.as_view()),
    path("transactions/deposits/", DepositViewSet.as_view({"post": "create"})),
    path("transactions/withdraw/", WithdrawView.as_view()),
]
