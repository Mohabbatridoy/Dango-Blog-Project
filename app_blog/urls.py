from django.urls import path
from app_blog import views

app_name = 'app_blog'
urlpatterns = [
    path('',views.BlogList.as_view(),name='blog_list'),
    path('create-blog/', views.CreateBlog.as_view(), name='create_blog'),

]