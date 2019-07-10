from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import MyUser
from main_app.models import Exam


class MyUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


# class ExaminerCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']
#
#
# class StudentCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
#
#
# class ExaminerLoginForm(forms.Form):
#     username = forms.CharField(max_length=128)
#     password = forms.CharField(max_length=128)
