
from rest_framework import permissions

class APILevelPermissionCheck(permissions.BasePermission):
    def has_permission(self, request, view):
        # Custom permission logic here
        return request.user and request.user.is_authenticated
