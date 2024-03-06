
from django.contrib import admin
from django.urls import path, include
from note.views import index, page_not_found, gf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('note.urls')),
    path('game_field', gf),

]


handler404 = page_not_found