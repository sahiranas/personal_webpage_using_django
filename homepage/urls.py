from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from homepage import views

urlpatterns = [
    path('',views.home, name='home'),
]
    