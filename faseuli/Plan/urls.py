from django.urls import path
from .views import *

urlpatterns = [
    path('main', plan_main, name="main"),
    path('add', plan_add, name="add"),
]
