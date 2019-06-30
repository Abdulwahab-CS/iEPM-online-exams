from django.contrib import admin

from .models import MyUser, Question, Exam, TakenExam

admin.site.register(MyUser)
admin.site.register(Question)
admin.site.register(Exam)
admin.site.register(TakenExam)

# from .models import ExaminerProfile, StudentProfile, Question, Exam, TakenExam
#
#
# admin.site.register(ExaminerProfile)
# admin.site.register(StudentProfile)
# admin.site.register(Question)
# admin.site.register(Exam)
# admin.site.register(TakenExam)
