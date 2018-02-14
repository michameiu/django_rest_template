from rest_framework.exceptions import APIException
from rest_framework.permissions import BasePermission


class MyCustomException(APIException):
    status_code = 503
    detail="Service temporarily unavailable, try again later."
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

    def __init__(self,message,code):
        self.status_code=code
        self.default_detail=message
        self.detail=message


class IsAuthenticatedOrOptions(BasePermission):
    safe_methods=["OPTIONS",]
    def has_permission(self, request, view):
        if request.method  in self.safe_methods:
            return True
        return request.user.is_authenticated()
