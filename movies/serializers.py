from rest_framework import serializers
from .models import MovieRate, Movie
from users.serializers import UserSerializer
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