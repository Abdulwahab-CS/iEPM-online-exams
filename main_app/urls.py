from django.urls import path

from . import views as users_views

app_name = "main"
urlpatterns = [
    path('', users_views.home, name="home"),
    path('all_exams/', users_views.all_exams, name='all_exams'),
    path('add_exam/', users_views.add_exam, name='add_exam'),
]
