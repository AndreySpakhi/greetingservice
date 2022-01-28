from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('greeted', views.greeted, name='greeted'),
]