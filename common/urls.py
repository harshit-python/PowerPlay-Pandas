from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', common_home, name="common-home"),
]
