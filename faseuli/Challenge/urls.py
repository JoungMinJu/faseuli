from django.urls import path
from .views import *

urlpatterns = [
    path('main/', challenge_main, name="main"),
    path('detail/', challenge_detail, name="detail"),
    path('write/', challenge_write, name="write"),
]
