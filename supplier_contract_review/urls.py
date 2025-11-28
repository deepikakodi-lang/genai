from django.urls import path
from .views import supplier_home

urlpatterns = [
    path("", supplier_home),
]
