from django.urls import path
from . import views as users_views


app_name = "users"
urlpatterns = [

    path('', users_views.home, name='home'),

    path('examiners/sign_up/', users_views.examiner_sign_up, name='examiner_sign_up'),
    path('students/sign_up/', users_views.student_sign_up, name='student_sign_up'),

    path('login/', users_views.the_login, name='login'),

    path('logout/', users_views.the_logout, name='logout'),

    # path('examiners/logout/', users_views.examiner_logout, name='examiner_logout'),
    # path('students/logout/', users_views.student_logout, name='student_logout'),

    path('examiners/<slug>/', users_views.examiner_profile, name='examiner_profile'),
    path('students/<slug>/', users_views.student_profile, name='student_profile'),

]

