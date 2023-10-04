
from django.contrib import admin
from django.urls import path, include
from note.views import index, page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('note.urls')),
]


handler404 = page_not_found