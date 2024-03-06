from django.contrib import admin
from .models import MovieDetails, bookedMovie




admin.site.register(MovieDetails)
admin.site.register(bookedMovie)