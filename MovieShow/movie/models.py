from django.contrib.auth.models import User
from django.db import models



class MovieDetails(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    



class bookedMovie(models.Model):
    movieStats = models.ForeignKey(MovieDetails, on_delete = models.CASCADE, null=True)
    booking = models.BooleanField(default=False, null=True)
    
    # def __str__(self):
    #   return self.booking
    