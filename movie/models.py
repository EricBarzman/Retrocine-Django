from django.db import models
from django.conf import settings


class Region(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Keyword(models.Model):
    label = models.CharField(max_length=255)
    def __str__(self):
        return self.label


class Country(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)
    class Meta:
        verbose_name_plural = 'Countries'
    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, related_name='directors', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ('last_name',)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    label = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    def __str__(self):
        return self.label


class Movie(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    year = models.IntegerField()
    country = models.ForeignKey(Country, related_name='movies', on_delete=models.SET_NULL, blank=True, null=True)
    genre = models.ForeignKey(Genre, related_name='movies', on_delete=models.SET_NULL, blank=True, null=True)
    director = models.ForeignKey(Director, related_name='movies', on_delete=models.SET_NULL, null=True)
    short_description = models.TextField(blank=True, null=True)
    
    DECADE_CHOICE = (
        ('1920s', '1920s'),
        ('1930s', '1930s'),
        ('1940s', '1940s'),
        ('1950s', '1950s'),
        ('1960s', '1960s'),
        ('1970s', '1970s'),
        ('1980s', '1980s'),
        ('1990s', '1990s'),
        ('2000s', '2000s'),
    )

    decade = models.CharField(max_length=5, choices=DECADE_CHOICE, null=True)
    keywords = models.ManyToManyField(Keyword)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)
    youtube_id = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.title
    
    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return 'https://placehold.co/600x400'