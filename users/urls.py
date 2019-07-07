from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as users_views


app_name = "users"
urlpatterns = [

    path('', users_views.home, name='home'),

    path('examiners/sign_up/', users_views.examiner_sign_up, name='examiner_sign_up'),
    path('students/sign_up/', users_views.student_sign_up, name='student_sign_up'),


    path('examiners/login/', auth_views.LoginView.as_view(template_name='users/examiners/examiner_login.html'),
         name='examiner_login'),

    path('students/login/', auth_views.LoginView.as_view(template_name='users/students/student_login.html'),
         name='student_login'),

    # path('examiners/login/', users_views.examiner_login, name='examiner_login'),
    # path('students/login/', users_views.student_login, name='student_login'),


    path('examiners/<slug>/', users_views.examiner_profile, name='examiner_profile'),
    path('students/<slug>/', users_views.student_profile, name='student_profile'),

]

