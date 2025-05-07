from django.urls import path
from app_login import views


app_name = 'app_login'
urlpatterns = [
    path('singup/', views.SingUp, name="singup"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('change_profile/', views.ProfileChang, name="chngProfile"),
    path('password/', views.pass_change, name="pass_change"),
    path('pro_pic_add/', views.Profile_pic_add, name="pro_pic_add"),
    path('change-pro-pic/', views.Change_Profile, name="change_pro_pic")
]