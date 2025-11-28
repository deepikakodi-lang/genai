from django.http import HttpResponse
from django.shortcuts import render


def medical_claims_home(request):

    return render(request, "medical_claims/MedicalClaimsAssistant.html")
