from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from movie.models import Movie


class Vote(models.Model):
    comment = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    movie = models.ForeignKey(Movie, related_name='votes', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='votes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_by} - {self.movie} - {self.rating}*"
    
    class Meta:
        ordering = ('-created_at',)



class Avatar(models.Model):
    label = models.CharField(max_length=255)
    image = models.ImageField(upload_to='avatars', blank=True, null=True)
    
    def __str__(self):
        return self.label
    
    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return 'https://placehold.co/600x400'



# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    avatar = models.ForeignKey(Avatar, blank=True, null=True, on_delete=models.SET_NULL)
    about = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.user.username



class UserFavorite(models.Model):
    user = models.ForeignKey(User, related_name='my_favorites', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='users_who_chose_as_favorite', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - {self.created_at}"
    
    class Meta:
        ordering = ('-created_at',)