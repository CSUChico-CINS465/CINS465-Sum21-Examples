from django.urls import path
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import LoginView
from django_otp.forms import OTPAuthenticationForm
#app level routing/urls

from . import views

urlpatterns = [
    path('', views.index),
    path('login/', auth_views.LoginView.as_view(authentication_form=OTPAuthenticationForm)),
    path('logout/', views.logout_view),
    path('register/', views.register_view),
    path('suggestions/', views.suggestions_view),
    path('suggestion/', views.suggestion_view),
    path('comment/<int:sugg_id>/', views.comment_view),
]
