from django.contrib import admin

from .models import Question, Exam, TakenExam

admin.site.register(Question)
admin.site.register(Exam)
admin.site.register(TakenExam)

