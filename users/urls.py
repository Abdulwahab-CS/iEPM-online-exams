from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as users_views


app_name = "users"
urlpatterns = [

    path('', users_views.home, name='home'),
    path('examiner/sign_up/', users_views.examiner_sign_up, name='examiner_sign_up'),
    path('student/sign_up/', users_views.student_sign_up, name='student_sign_up'),


    path('examiner/login/', auth_views.LoginView.as_view(template_name='users/examiner_login.html'),
         name='examiner_login'),

    path('student/login/', auth_views.LoginView.as_view(template_name='users/student_login.html'),
         name='student_login'),

    path('examiner/<slug>/', users_views.examiner_profile, name='examiner_profile'),
    path('student/<slug>/', users_views.student_profile, name='student_profile'),

    path('examiner/add_exam/', users_views.add_exam, name='add_exam'),

]

