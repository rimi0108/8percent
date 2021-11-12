from django.urls import path

from apps.eightpercent.views import TransactionView

app_name = "eightpercent"

urlpatterns = [
    path("transactions", TransactionView.as_view()),
]
