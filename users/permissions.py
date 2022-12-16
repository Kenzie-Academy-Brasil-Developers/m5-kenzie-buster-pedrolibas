from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user.id:
            user = User.objects.get(username=request.user).is_superuser

            if request.user.is_authenticated and user:
                return True

        return False
        

class IsLogged(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.user.id:
            return True

        return False