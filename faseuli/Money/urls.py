from django.urls import path
from . import views

app_name="money"
urlpatterns = [
    path('main', views.money_main, name="main"),
    path('record', views.money_record, name="record"),
]