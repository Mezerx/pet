from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django import forms
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView, FormView, DeleteView

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
            return redirect(game_field)
    else:
        form = AddUsers()
    data = {
        "form": form,
        }

    return render(request, 'note/index.html',data)




def page_not_found(request , exeption):
    return HttpResponseNotFound("<h1>404 Not Found</h1>")

def gf(request):
    t = render_to_string('note/game_field.html')
    return HttpResponse(t)

def game_field(request):
    posts = User.objects.all()
    data = {
        'title':'Game Field',
        'posts': posts,
    }
    return render(request, 'note/game_field.html', context=data)



def gg(request):

    if request.method == 'POST':
        gg = User.objects.all()
        gg.clear()
        gg.save()
        return redirect('home')
    else:
        gg = User.objects.all().delete()
        return redirect('home')

    data = {
        "gg" : gg,
    }

    return render(request, 'note/game_field.html', context=data)
