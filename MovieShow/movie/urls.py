from django.urls import path
from . import views



urlpatterns = [
  path('', views.movies, name='movies'),
  path('movieOne/<str:id>/', views.movieOne, name='movieOne'),
  path('new/', views.newMovie, name='new'),
  path('edit/<str:pk>/', views.editMovie, name='edit'),
  path('delete/<str:id>/', views.deleteMovie, name='delete'),
  path('book/', views.bookMovie, name='book'),
]
