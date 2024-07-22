from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Avatar, UserFavorite, Vote, Profile
from movie.models import Movie

from .serializers import Avatar_serializer, Vote_serializer, User_detail_serializer
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

    # Filtrer les movies dont la pk est inclus dans la liste des favorites, dans leur movie.id
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



# Return all ratings from current user (to check if he already voted)
@api_view(['GET'])
def get_all_user_ratings(request):
    votes = Vote.objects.filter(created_by=request.user)
    serializer = Vote_serializer(votes, many=True)
    return Response(serializer.data)



# Process a vote
@api_view(['POST'])
def rate_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    data = request.data
    Vote.objects.create(
        movie=movie,
        created_by=request.user,
        comment=data.get('comment'),
        rating=int(data.get('rating'))
    )

    return Response({ 'message' : 'You have voted!'})


@api_view(['GET'])
def get_user_infos(request):
    profile = Profile.objects.get(user=request.user.id)  
    serializer = User_detail_serializer(profile)
    return Response(serializer.data)


@api_view(['POST'])
def change_avatar(request):
    return Response({ 'message' : 'Successful' })