from django.urls import path
from . import views

urlpatterns = [
    # takes 2 arguments, 
    # path/route
    # view function
    # path("january", views.january),
    # path("february", views.february),
    # placeholder syntax (dynamic path/url)
    path('', views.index),
    path('<int:month>', views.monthly_challenge_by_number),
    path('<str:month>', views.monthly_challenge, name='monthly-challenge'),
]

