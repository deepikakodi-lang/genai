from django.urls import path
from .views import logistic_home

urlpatterns = [
    path("", logistic_home),
]
