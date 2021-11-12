from rest_framework.permissions import BasePermission, IsAuthenticated


class IsAccountOwnerOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj.customer.id == request.user.id
