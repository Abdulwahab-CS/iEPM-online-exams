from django.contrib.auth.models import User
# from src.main_app.models import ExaminerProfile, StudentProfile
from django.contrib.auth.forms import UserCreationForm

from main_app.models import MyUser


class ExaminerCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        # def save(self, commit=True):
        #     user = super().save(commit=False)
        #     user.is_examiner = True
        #     if commit:
        #         user.save()
        #     return user


class StudentCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
