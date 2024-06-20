from django.urls import path
from . import views

urlpatterns = [
    # path('get-personal-information', views.get_personal_information),
    path('vote-for-movie', views.get_all_user_ratings),
    path('vote-for-movie/<int:movie_id>', views.rate_movie),
    # path('most-popular-movies/', views.get_most_popular_movies),
    path('avatars/', views.get_avatars),
    path('my-favorites/', views.get_my_favorites),
    path('my-favorites/add/<int:movie_id>', views.add_a_favorite),
    path('my-favorites/remove/<int:movie_id>', views.remove_a_favorite),
]