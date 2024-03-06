from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django import forms

from note.forms import AddUsers
from note.models import User


def index(request):
    if request.method == 'POST':
        form = AddUsers(request.POST)
        if form.is_valid():

           # try:
            #    User.objects.create(**form.cleaned_data)
           #     return redirect('')

          #  except:
           #     form.add_error(None,'Invalid')
       # print(form.cleaned_data)
            form.save()
            return redirect(gf)
    else:
        form = AddUsers()
    data = {
        "form": form,
        }

    return render(request, 'note/index.html',data)




def page_not_found(request , exeption):
    return HttpResponseNotFound("<h1>404 Not Found</h1>")

def gf(request):
    return HttpResponse('<h1>Game Field</h1>')
