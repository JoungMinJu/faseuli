from django.urls import path
from .views import *

urlpatterns = [
    path('main/', plan_main, name="main"),
    path('add/', plan_add, name="add"),
    path('create/',plan_create, name='create'),
    path('del/<str:id>',plan_del,name='del'),
    path('edit/<str:id>',edit_plan, name='edit'),
    path('update/<str:id>',update_plan, name='update'),
]
