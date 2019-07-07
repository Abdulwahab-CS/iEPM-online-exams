from django.shortcuts import render, redirect
from .forms import AddExamForm
from .models import Exam, Question
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages


def home(request):
    return render(request, 'main_app/home.html')


def add_exam(request):

    if request.method == 'POST':
        form = AddExamForm(request.POST)

        if form.is_valid():
            exam_name = form.cleaned_data.get('exam_name')
            category = form.cleaned_data.get('category')
            # create new exam
            Exam.objects.get_or_create(examiner=request.user.myuser, exam_name=exam_name, category=category)

            return redirect('main:all_exams')

    else:
        form = AddExamForm()

    data = {
        'form': form
    }
    return render(request, 'main_app/add_exam.html', data)


def all_exams(request):

    exams = Exam.objects.filter(examiner=request.user.myuser)
    for exam in exams:
        n = Question.objects.filter(exam=exam)
        exam.num_of_questions = len(n)

    data = {
        'exams': exams,
        'current_user': request.user.myuser,
        'exams_count': range(len(exams))
    }
    return render(request, 'main_app/all_exams.html', data)


def delete_exam(request, exam_id):
    exam_to_delete = ""
    if request.method == 'POST':
        exam = get_object_or_404(Exam, id=exam_id)
        exam_to_delete = exam.exam_name
        exam.delete()

    messages.success(request, f" ( {exam_to_delete} Exam ) deleted successfully")
    return redirect('main:all_exams')
