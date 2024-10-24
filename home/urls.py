from django.urls import path

from . import views


urlpatterns = [
    path('home/', views.home, name='home-home'),
    path('authenticated/', views.authenticated, name='home-authenticated'),
]
