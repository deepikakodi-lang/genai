from django.http import HttpResponse
from django.shortcuts import render


def logistic_home(request):
    return render(request, "logistic/logistic_bot.html")
