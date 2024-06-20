from django.contrib import admin
from .models import Vote, Avatar, UserFavorite, User_Info

admin.site.register(Vote)
admin.site.register(Avatar)
admin.site.register(User_Info)
admin.site.register(UserFavorite)