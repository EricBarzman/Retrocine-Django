from rest_framework import serializers
from .models import Movie, Country, Director, Keyword, Genre
from votes.serializers import Vote_serializer


class Country_serializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class Director_serializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'first_name', 'last_name')


class Genre_serializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'label', 'slug')


class Keyword_serializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ('id', 'label')



class Movie_serializer(serializers.ModelSerializer):
    director = Director_serializer(many=False)
    country = Country_serializer(many=False)
    genre = Genre_serializer(many=False)
    keywords = Keyword_serializer(many=True)

    class Meta:
        model = Movie
        fields = (
            'id', 'title', 'slug', 'director', 'country',
            'year', 'genre', 'decade', 'short_description',
            'get_image', 'youtube_id', 'keywords', 'average_rating',
            'number_of_votes',
        )


# Like previous, plus ALL the votes associated !
class Movie_detailed_serializer(serializers.ModelSerializer):
    director = Director_serializer(many=False)
    country = Country_serializer(many=False)
    genre = Genre_serializer(many=False)
    keywords = Keyword_serializer(many=True)
    votes = Vote_serializer(many=True)

    class Meta:
        model = Movie
        fields = (
            'id', 'title', 'slug', 'director', 'country',
            'year', 'genre', 'decade', 'short_description',
            'get_image', 'youtube_id', 'keywords', 'average_rating',
            'number_of_votes', 'votes'
        )