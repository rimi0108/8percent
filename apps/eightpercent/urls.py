from django.urls import path

from apps.eightpercent.views import AccountView, WithdrawView

app_name = "eightpercent"

urlpatterns = [
    path("account/", AccountView.as_view()),
    path("transactions/withdraw/", WithdrawView.as_view()),
]
