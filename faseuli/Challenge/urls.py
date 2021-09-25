from django.urls import path
from . import views

urlpatterns = [
    path('main', views.challenge_main, name="main"),
    path('detail', views.challenge_detail, name="detail"),
    path('write', views.challenge_write, name="write"),
    path('new_history', views.new_history, name="new_history")
]