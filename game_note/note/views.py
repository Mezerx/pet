from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>главная страница приложения note</h1>")




def page_not_found(request , exeption):
    return HttpResponseNotFound("<h1>404 Not Found</h1>")