from django.contrib import admin
from .models import Vote, Avatar, UserFavorite

admin.site.register(Vote)
admin.site.register(Avatar)
admin.site.register(UserFavorite)