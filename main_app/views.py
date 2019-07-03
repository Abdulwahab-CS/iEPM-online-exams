from django.shortcuts import render, redirect
from .forms import AddExamForm
from .models import Exam


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

            path = f"/users/examiner/{request.user.myuser.slug}/"
            return redirect(path)

    else:
        form = AddExamForm()

    data = {
        'form': form
    }
    return render(request, 'main_app/add_exam.html', data)


def all_exams(request):

    exams = Exam.objects.all()

    data = {
        'exams': exams
    }
    return render(request, 'main_app/all_exams.html', data)
