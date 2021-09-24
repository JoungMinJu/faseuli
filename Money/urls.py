from django.urls import path
from .views import *

urlpatterns = [
    path('main/', money_main, name="main"),
    path('record/', money_record, name="record"),
]
