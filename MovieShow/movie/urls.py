from django.urls import path
from . import views



urlpatterns = [
  path('', views.movies, name='movies'),
  path('movieOne/<int:id>/', views.movieOne, name='movieOne'),
  path('new/', views.newMovie, name='new'),
  path('edit/', views.editMovie, name='edit'),
  path('book/', views.bookMovie, name='book'),
]