from django.urls import path

from apps.eightpercent.views import AccountView

app_name = "eightpercent"

urlpatterns = [
    path("account/", AccountView.as_view()),
]
