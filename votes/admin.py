from django.contrib import admin
from .models import Vote, Avatar, UserFavorite, Profile

admin.site.register(Vote)
admin.site.register(Avatar)
admin.site.register(Profile)
admin.site.register(UserFavorite)