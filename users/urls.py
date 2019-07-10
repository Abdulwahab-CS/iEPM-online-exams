from django.urls import path
from . import views as users_views


app_name = "users"
urlpatterns = [

    path('', users_views.home, name='home'),

    path('examiners/sign_up/', users_views.examiner_sign_up, name='examiner_sign_up'),
    path('students/sign_up/', users_views.student_sign_up, name='student_sign_up'),

    path('examiners/login/', users_views.examiner_login, name='examiner_login'),
    path('students/login/', users_views.student_login, name='student_login'),

    path('examiners/logout/', users_views.examiner_logout, name='examiner_logout'),
    path('students/logout/', users_views.student_logout, name='student_logout'),

    path('examiners/<slug>/', users_views.examiner_profile, name='examiner_profile'),
    path('students/<slug>/', users_views.student_profile, name='student_profile'),

]

