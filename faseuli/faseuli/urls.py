from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from User import views
# from Plan.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path('', home, name="home"),
    
    path('user/signup', views.signup_view, name="signup"),
    path('user/login', views.login_view, name="login"),
    path('user/logout', views.logout_view, name="logout"),
    
    path('', views.home, name="home"),

    path('plan/', include('Plan.urls')),
    path('challenge/', include('Challenge.urls')),
    path('money/', include('Money.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)