""" urls for webapp app """

from django.urls import path
from . import views

APP_NAME = 'webapp'

urlpatterns = [
    path('', views.index, name='index'),
]