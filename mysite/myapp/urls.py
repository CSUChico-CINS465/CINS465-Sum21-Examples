from django.urls import path
from django.contrib.auth import views as auth_views
#app level routing/urls 

from . import views

urlpatterns = [
    path('', views.index),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', views.logout_view),
    path('register/', views.register_view),
    path('suggestions/', views.suggestion_view),
]