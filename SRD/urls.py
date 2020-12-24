""" urls for SRD app """

from django.urls import path
from . import views

APP_NAME = 'SRD'

urlpatterns = [
    path('SRD/home', views.SRDManagement().SRD_home, name='SRD_home'),
]