from django.urls import path
from .views import underwriter_home

urlpatterns = [
    path("", underwriter_home),
]
