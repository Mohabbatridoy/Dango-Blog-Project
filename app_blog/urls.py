from django.urls import path
from app_blog import views

app_name = 'app_blog'
urlpatterns = [
    path('',views.blog_list,name='blog_list')
]