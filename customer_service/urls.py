from django.urls import path
from . import views

urlpatterns = [
    path('get-topics/', views.get_topics),
    path('send-issue/', views.register_issue_message)
]