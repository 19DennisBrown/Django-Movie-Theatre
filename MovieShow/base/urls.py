from django.urls import path
from . import views
# from userAuth import views


urlpatterns = [
  path('home/', views.home, name='home'),
  # path('', views.user, name='user')
]