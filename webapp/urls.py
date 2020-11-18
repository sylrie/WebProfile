""" urls for webapp app """

from django.urls import path
from . import views

APP_NAME = 'webapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('tools', views.tools, name='tools'),
    path('credits', views.credits, name='credits'),

    path('contact-mail', views.contact_mail, name='contact_mail'),
]