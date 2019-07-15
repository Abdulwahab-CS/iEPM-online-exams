
from django import forms
from .models import Exam


class AddExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['exam_name', 'category']


class EditExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['exam_name', 'category']
