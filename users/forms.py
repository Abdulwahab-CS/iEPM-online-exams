from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from users.models import MyUser
from main_app.models import Exam


class ExaminerCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class StudentCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']


class AddExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['exam_name', 'category', 'published']
