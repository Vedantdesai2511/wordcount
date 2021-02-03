from django.http import HttpResponse
from django.shortcuts import render


def colorgame(request):
    return render(request, 'colorGame.html')
