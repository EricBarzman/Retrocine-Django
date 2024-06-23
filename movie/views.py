from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Movie, Genre, Country
from .serializers import Movie_serializer, Movie_detailed_serializer, Genre_serializer, Country_serializer

# All films
@api_view(['GET'])
def get_movies(request):
    movies = Movie.objects.order_by('?')
    serializer = Movie_serializer(movies, many=True)
    return Response(serializer.data)

# One film with all details
@api_view(['GET'])
def get_movie(request, slug):
    movie = Movie.objects.get(slug=slug)
    serializer = Movie_detailed_serializer(movie)
    return Response(serializer.data)

# Search by keyword
@api_view(['POST'])
def search_for_movies(request):
    data = request.data
    movies = Movie.objects.filter(title__icontains=data.get('searchInput'))
    serializer = Movie_serializer(movies, many=True)
    return Response(serializer.data)


# One random film
@api_view(['GET'])
def get_random_movie(request):
    movie = Movie.objects.order_by('?')[0]
    serializer = Movie_serializer(movie)
    return Response(serializer.data)

# Five random films
@api_view(['GET'])
def get_five_random_movies(request):
    movies = Movie.objects.order_by('?')[0:5]
    serializer = Movie_serializer(movies, many=True)
    return Response(serializer.data)


# Get movies by genre
@api_view(['GET'])
def get_movies_by_genre(request, genre_id):
    movies = Movie.objects.filter(genre=genre_id)
    serializer = Movie_serializer(movies, many=True)
    return Response(serializer.data)

# Get all genres
@api_view(['GET'])
def get_genres(request):
    genres = Genre.objects.all()
    serializer = Genre_serializer(genres, many=True)
    return Response(serializer.data)

# Get movies by country
@api_view(['GET'])
def get_movies_by_country(request, country_id):
    movies = Movie.objects.filter(country=country_id)
    serializer = Movie_serializer(movies, many=True)
    return Response(serializer.data)

# Get all countries
@api_view(['GET'])
def get_countries(request):
    countries = Country.objects.all()
    serializer = Country_serializer(countries, many=True)
    return Response(serializer.data)