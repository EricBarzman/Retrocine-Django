from django.contrib import admin
from .models import Country, Director, Movie, Region, Genre, Keyword

admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Keyword)
