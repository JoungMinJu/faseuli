from django.urls import path
from . import views

urlpatterns = [
    path('main', views.money_main, name="main"),
    path('record', views.money_record, name="record"),
]