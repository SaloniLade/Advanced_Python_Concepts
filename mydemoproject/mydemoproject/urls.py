from django.contrib import admin
from django.urls import path
from .views import demo, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', demo),
    path('', home),
]