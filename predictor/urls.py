from django.urls import path
from . import views

urlpatterns = [
    path('heart', views.heart, name="heart"),
    
    path('breast', views.breast, name="breast"),
    path('', views.home, name="home"),
]
