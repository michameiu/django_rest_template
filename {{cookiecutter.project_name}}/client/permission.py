from rest_framework.permissions import BasePermission
SAFE_METHODS = ['POST', 'HEAD', 'OPTIONS']

class IsAuthenticatedOrPOSTOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """
    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated()):
            return True
        return False

class IsOwner(BasePermission):
    def has_object_permission(self, request, view , obj):
        return obj.user.id == request.user.id