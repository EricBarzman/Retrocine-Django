from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.get_movies),
    path('search/', views.search_for_movies),
    path('random/', views.get_random_movie),
    path('index/<slug:slug>/', views.get_movie),
    path('genre/', views.get_genres),
    path('genre/<int:genre_id>', views.get_movies_by_genre),
    path('country/', views.get_countries),
    path('country/<int:country_id>', views.get_movies_by_country),
    path('pick-of-the-week/', views.get_five_random_movies),
]