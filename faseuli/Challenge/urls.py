from django.urls import path
from . import views

app_name='challenge'
urlpatterns = [
    path('main', views.challenge_main, name="main"),
    path('detail/<str:id>', views.challenge_detail, name="detail"),
    path('write', views.challenge_write, name="write"),
    path('new_history/<str:id>', views.new_history, name="new_history"),
    path('delete/<str:id>', views.challenge_delete, name="delete"),
]