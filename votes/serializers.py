from rest_framework import serializers
from .models import Vote, Avatar, UserFavorite, User_Info
from django.contrib.auth.models import User

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')

class User_detail_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class Avatar_serializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = ('id', 'label', 'get_image')



class User_favorites_serializer(serializers.ModelSerializer):
    class Meta:
        model = UserFavorite
        fields = ('id', 'user', 'movie', 'created_at')


class Vote_serializer(serializers.ModelSerializer):
    created_by = User_Serializer(many=False)
    class Meta:
        model = Vote
        fields = ('id', 'created_by', 'movie', 'created_at', 'rating', 'comment')