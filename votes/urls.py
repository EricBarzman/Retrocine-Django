from django.urls import path
from . import views

urlpatterns = [
    path('avatars/', views.get_avatars),
    path('my-favorites/', views.get_my_favorites),
    path('my-favorites/add/<int:movie_id>', views.add_a_favorite),
    path('my-favorites/remove/<int:movie_id>', views.remove_a_favorite),
]