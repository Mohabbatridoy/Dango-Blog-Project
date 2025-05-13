from django.urls import path
from app_blog import views

app_name = 'app_blog'
urlpatterns = [
    path('',views.BlogList.as_view(),name='blog_list'),
    path('create-blog/', views.CreateBlog.as_view(), name='create_blog'),
    path('blog-details/<path:slug>', views.blog_details, name="blog_details"),
    path('liked/<pk>/', views.Liked, name="liked_post"),
    path('uliked/<pk>/', views.Unliked, name="unliked_post"),
    path('my-blog/', views.MyBlog.as_view(), name="myblog"),
    path('edit-blog/<pk>/', views.EditBlog.as_view(), name="edit_blog"),
]