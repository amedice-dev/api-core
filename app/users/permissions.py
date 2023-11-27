from rest_framework import permissions


class IsVisitor(permissions.BasePermission):
    """
    Check if user is a Visitor.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Visitors').exists()


class IsOwner(permissions.BasePermission):
    """
    Check if user is an Owner.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Owners').exists()


class IsOrgAdmin(permissions.BasePermission):
    """
    Check if user is an Organisation Admin.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Administrators').exists()
