from django.urls import path
from . import views

urlpatterns = [
    path('avatars/', views.get_avatars),
]