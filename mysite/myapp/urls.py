from django.urls import path
#app level routing/urls 

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:page>/', views.index),
]