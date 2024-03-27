from django.urls import path
from . import views
from .views import gf

urlpatterns = [

    path('', views.index, name='home'),
    path('game_field', views.game_field),
    path('gg', views.gg, name='gg'),


]
