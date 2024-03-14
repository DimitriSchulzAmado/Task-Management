from django.contrib import admin
from django.urls import path

from todos.views import home

# Rotes and what view to call
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
