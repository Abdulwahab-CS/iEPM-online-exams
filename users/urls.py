from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as users_views


app_name = "users"
urlpatterns = [
    path('', users_views.home, name="home"),
    path('examiner/sign_up/', users_views.examiner_sign_up, name="examiner_sign_up"),
    path('examiner/login/', auth_views.LoginView.as_view(template_name='users/examiner_login.html'),
         name="examiner_login"),

    path('examiner/logout/', auth_views.LogoutView.as_view(template_name='users/examiner_logout.html'),
         name="examiner_logout"),
]
