from django.contrib import admin
from .models import Movie, bookedMovie
# Register your models here.
admin.site.register(Movie)
admin.site.register(bookedMovie)