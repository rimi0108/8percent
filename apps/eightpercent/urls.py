from django.urls import path

from apps.eightpercent.views import AccountCreateView, AccountView

app_name = "eightpercent"

urlpatterns = [
    path("account/", AccountView.as_view()),
    # path("account/<str:pk>/", AccountView.as_view()),
]
