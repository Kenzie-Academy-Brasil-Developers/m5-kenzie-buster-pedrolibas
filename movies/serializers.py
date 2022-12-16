from rest_framework import serializers
from .models import MovieRate, Movie, MovieOrder
from users.models import User

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField(allow_null=True, default=None)
    rating = serializers.ChoiceField(choices=MovieRate.choices, default=MovieRate.G, allow_null=True)
    synopsis = serializers.CharField(allow_null=True, default=None)
    added_by = serializers.SerializerMethodField(read_only=True)

    def get_added_by(self, obj):
        return User.objects.get(id=obj.user.id).email

    def create(self, validated_data: dict):
        print(validated_data)
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.FloatField()
    title = serializers.SerializerMethodField(read_only=True)
    buyed_by = serializers.SerializerMethodField(read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)
    
    def get_title(self, obj):
        return obj.movie.title

    def get_buyed_by(self, obj):
        return obj.user.email

    def create(self, validated_data: dict):
        return MovieOrder.objects.create(**validated_data)