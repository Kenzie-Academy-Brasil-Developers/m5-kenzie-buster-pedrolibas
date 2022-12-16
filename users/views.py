from rest_framework.views import APIView, Response, Request, status
from .serializers import UserSerializer
from .permissions import IsLogged
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User
from django.shortcuts import get_object_or_404

class RegisterView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLogged]
    
    def get(self, request: Request, user_id: int):
        user_accessing = User.objects.get(username=request.user)
        user_accessed = User.objects.get(id=user_id)
        serializer = UserSerializer(user_accessed)

        if user_accessing.is_superuser:
            return Response(serializer.data)

        if user_accessing.id == serializer.data["id"]:
            return Response(serializer.data)

        return Response(status=status.HTTP_403_FORBIDDEN)