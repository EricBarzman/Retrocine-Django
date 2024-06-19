from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Avatar, UserFavorite
from movie.models import Movie

from .serializers import Avatar_serializer, User_favorites_serializer
from movie.serializers import Movie_serializer


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_avatars(request):
    avatars = Avatar.objects.all()
    serializer = Avatar_serializer(avatars, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_my_favorites(request):
    favorites = UserFavorite.objects.filter(user=request.user.id)
    my_favorite_movies = []

    # Filter les movies dont la pk est inclus dans la liste des favorites, dans leur movie.id
    for favorite in favorites:
        movie = Movie.objects.get(pk=favorite.movie.id)
        if movie:
            my_favorite_movies.append(movie)
    
    serializer = Movie_serializer(my_favorite_movies, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def add_a_favorite(request, movie_id):    
    movie = Movie.objects.get(pk=movie_id)
    
    favorites = UserFavorite.objects.filter(user=request.user, movie=movie)
    
    if favorites:
        return Response({ 'message' : 'Movie is already a favorite'})

    new_favorite = UserFavorite.objects.create(user=request.user, movie=movie)
    return Response({ 'message' : 'Movie was added to favorite!' })



@api_view(['GET'])
def remove_a_favorite(request, movie_id):

    movie = Movie.objects.get(pk=movie_id)
    favorites = UserFavorite.objects.filter(user=request.user, movie=movie)
    if not favorites:
        return Response({ 'message' : 'Movie is not a favorite and could not be removed' })
    
    favorites[0].delete()
    return Response({ 'message' : 'Favorite removed successfully' })