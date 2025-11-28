from django.urls import path
from .views import medical_claims_home

urlpatterns = [
    path("", medical_claims_home),
]
