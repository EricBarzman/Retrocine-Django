from rest_framework import serializers
from .models import Vote, Avatar, UserFavorite


class Avatar_serializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = ('id', 'label', 'get_image')


class User_favorites_serializer(serializers.ModelSerializer):
    class Meta:
        model = UserFavorite
        fields = ('id', 'user', 'movie', 'created_at')