from django.urls import path
from . import views

app_name='plan'
urlpatterns = [
    path('main/', views.main, name="main"),
    path('add/', views.plan_add, name="add"),
    path('create/',views.plan_create, name='create'),
    path('del/',views.plan_del,name='del'),
    path('edit/',views.edit_plan, name='edit'),
    path('update/',views.update_plan, name='update'),
]
