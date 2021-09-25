from django.urls import path
from . import views

urlpatterns = [
    path('main', views.challenge_main, name="main"),
    path('detail/<str:id>/', views.challenge_detail, name="Challenge_detail"),
    path('write/', views.challenge_write, name="write"),
    path('new_history/<str:id>', views.new_history, name="new_history")
]