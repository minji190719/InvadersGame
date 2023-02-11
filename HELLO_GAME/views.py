from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse


def game(request):
    return render(request, 'game03.html')
