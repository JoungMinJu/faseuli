from django.urls import path
from . import views

urlpatterns = [
    path('main', views.challenge_main, name="main"),
    path('detail/<int:id>', views.challenge_detail, name="detail"),
    path('write/<int:id>', views.challenge_write, name="write"),
    path('new_history/<int:id>', views.new_history, name="new_history")
]