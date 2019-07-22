from django.urls import path

from . import views as users_views

app_name = "main"
urlpatterns = [
    path('', users_views.home, name="home"),
    path('add_exam/', users_views.add_exam, name='add_exam'),
    path('all_exams/', users_views.all_exams, name='all_exams'),
    path('delete_exam/<int:exam_id>/', users_views.delete_exam, name='delete_exam'),

    path('manage_exam/<int:exam_id>/add_question/', users_views.add_question, name='add_question'),
    path('manage_exam/<int:exam_id>/edit_exam/', users_views.edit_exam, name='edit_exam'),
    path('manage_exam/<int:exam_id>/show_exam/', users_views.show_exam, name='show_exam'),
    path('manage_exam/<int:exam_id>/do_edit_exam/', users_views.do_edit_exam, name='do_edit_exam'),

    path('manage_exam/<int:exam_id>/manage_questions/', users_views.manage_questions, name='manage_questions'),

    path('do_exam/<int:exam_id>/', users_views.do_exam, name='do_exam'),
    path('update_question/<int:exam_id>/<int:question_id>/', users_views.update_question, name='update_question'),
    path('delete_question/<int:exam_id>/<int:question_id>/', users_views.delete_question, name='delete_question'),
    path('delete_exam/<int:exam_id>/', users_views.delete_exam, name='delete_exam'),
    path('submit_exam/', users_views.submit_exam, name='submit_exam'),
    path('students_scores/', users_views.students_scores, name='students_scores'),

    path('clear_scores/', users_views.clear_scores, name='clear_scores'),

    path('publish_exam/<int:exam_id>/', users_views.publish_exam, name='publish_exam'),
    path('un_publish_exam/<int:exam_id>/', users_views.un_publish_exam, name='un_publish_exam')
]
