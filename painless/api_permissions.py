from rest_framework import permissions


class IsStaffModifier(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['DELETE', 'POST', 'PUT'] and request.user.is_staff:
            return True
        else:
            return False