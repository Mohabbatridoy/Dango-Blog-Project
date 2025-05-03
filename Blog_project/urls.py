from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('log_in/', include('app_login.urls')),
    path('blog/', include('app_blog.urls')),
    path('', views.index, name="index"),
]
