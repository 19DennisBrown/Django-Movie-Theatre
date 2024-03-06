from django.contrib.auth.models import User
from django.db import models



class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Moviename(models.Model):
    title = models.ForeignKey(Movie, on_delete=models.CASCADE)
    def __str__(self):
      return self.title

class Moviedescription(models.Model):
    description = models.ForeignKey(Movie, on_delete=models.CASCADE)
    def __str__(self):
      return self.description

class Moviedate(models.Model):
    date = models.ForeignKey(Movie, on_delete=models.CASCADE)
    def __str__(self):
      return self.date

class Moviecost(models.Model):
    cost = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
      return self.cost


class bookedMovie(models.Model):
    title = models.ForeignKey(Moviename, on_delete=models.CASCADE)
    description = models.ForeignKey(Moviedescription, on_delete=models.CASCADE)
    day = models.ForeignKey(Moviedate, on_delete=models.CASCADE)
    cost = models.ForeignKey(Moviecost, on_delete=models.CASCADE)
    isBooked = models.BooleanField(default = False)

    def __str__(self):
      return self.title