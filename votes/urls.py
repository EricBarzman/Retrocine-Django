from django.urls import path
from . import views

urlpatterns = [
    path('vote-for-movie', views.get_all_user_ratings),
    path('vote-for-movie/<int:movie_id>', views.rate_movie),
    path('avatars/', views.get_avatars),
    path('my-favorites/', views.get_my_favorites),
    path('my-favorites/add/<int:movie_id>', views.add_a_favorite),
    path('my-favorites/remove/<int:movie_id>', views.remove_a_favorite),
    path('user-infos/', views.get_user_infos),
    path('change-avatar/', views.change_avatar),
]