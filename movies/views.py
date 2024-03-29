from rest_framework.views import APIView, Response, Request, status
from .models import Movie
from .serializers import MovieSerializer, MovieOrderSerializer
from users.permissions import IsAdminOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import User
from django.shortcuts import get_object_or_404
from users.permissions import IsLogged
from rest_framework.pagination import PageNumberPagination

class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    page_size = 2

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        result_movies = self.paginate_queryset(movies, request)
        serializer = MovieSerializer(result_movies, many=True)

        return self.get_paginated_response(serializer.data)
    
    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(username=request.user)
        serializer.save(user=user)

        return Response(serializer.data, status.HTTP_201_CREATED)

class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request, movie_id: int):
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)

        return Response(serializer.data)

    def delete(self, request: Request, movie_id: int):
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLogged]

    def post(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(username=request.user)
        serializer.save(movie=movie, user=user)

        return Response(serializer.data, status.HTTP_201_CREATED)