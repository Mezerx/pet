from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>главная страница приложения note</h1>")
