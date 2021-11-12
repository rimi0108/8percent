from rest_framework import status
from rest_framework.generics import (
    GenericAPIView,
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.eightpercent.models import Account
from apps.eightpercent.serializers import (
    CreateAccountSerializer,
    ReadAccountSerializer,
)


class AccountCreateView(CreateAPIView):

    queryset = None
    serializer_class = CreateAccountSerializer
    permission_class = IsAuthenticated

    def create(self, request, *args, **kwargs):
        has_account = Account.objects.filter(customer=request.user.id).first()
        if has_account is None:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                self.perform_create(serializer)
                return Response(
                    {"message": "Account is Created."},
                    status=status.HTTP_201_CREATED,
                )
        return Response(
            {"error": "Account already exist."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def perform_create(self, serializer):

        serializer.save(customer=self.request.user, balance=0)


class AccountView(CreateModelMixin, ListModelMixin, GenericAPIView):

    queryset = None
    permission_class = IsAuthenticated

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        account = self.get_queryset().first()
        serializer = self.get_serializer(account)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadAccountSerializer
        elif self.request.method == "POST":
            return ReadAccountSerializer

    def get_queryset(self):
        if self.request.method == "GET":
            return Account.objects.filter(customer=self.request.user.id)
        elif self.request.method == "POST":
            return None

    def create(self, request, *args, **kwargs):
        has_account = Account.objects.filter(customer=request.user.id).first()
        if has_account is None:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                self.perform_create(serializer)
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED,
                )
        return Response(
            {"error": "Account already exist."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def perform_create(self, serializer):

        serializer.save(customer=self.request.user, balance=0)
