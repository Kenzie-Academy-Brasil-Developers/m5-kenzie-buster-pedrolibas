from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User

class IsLogged(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.user.id:
            return True

        return False