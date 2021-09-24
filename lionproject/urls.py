from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from lion.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('challenge/', include('challenge.urls')),
    path('money/', include('money.urls')),
]
