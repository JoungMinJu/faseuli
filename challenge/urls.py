from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main, name="main"),
    path('detail/', detail, name="detail"),
    path('write/', write, name="write"),
]
