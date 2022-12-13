from rest_framework.views import APIView, Response, Request, status
from .serializers import UserSerializer

class RegisterView(APIView):
    def get(self, request: Request) -> Response:
        ...

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

