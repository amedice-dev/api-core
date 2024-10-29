from rest_framework import permissions


class IsVisitor(permissions.BasePermission):
    """
    Check if user is a Visitor.
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Visitors").exists()


class IsOwner(permissions.BasePermission):
    """
    Check if user is an Owner.
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Owners").exists()


class IsOrgAdmin(permissions.BasePermission):
    """
    Check if user is an Organisation Admin.
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Administrators").exists()


class CanUpdateOrganisation(permissions.BasePermission):
    """
    Check if user is in org_owner or org_admins fields.
    """

    def has_object_permission(self, request, view, obj):
        return request.user in obj.org_admins.all() or request.user == obj.org_owner


class IsSuperUser(permissions.BasePermission):
    """
    Allows access only to superusers.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
