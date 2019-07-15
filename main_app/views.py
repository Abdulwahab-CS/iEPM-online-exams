from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import AddExamForm, EditExamForm
from .models import Exam, Question
from django.shortcuts import get_object_or_404
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
            messages.success(request, f"( {exam_name} exam ) added successfully")
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


def manage_exam(request, exam_id):

    exam = Exam.objects.get(id=exam_id)
    exam_name = exam.exam_name
    exam_category = exam.category

    questions = Question.objects.filter(exam=exam)

    data = {
        'exam_id': exam_id,
        'exam_name': exam_name,
        'exam_category': exam_category,
        'questions': questions
    }

    return render(request, 'main_app/manage_questions.html', data)


def add_question(request, exam_id):
    if request.method == 'POST':

        exam = Exam.objects.get(id=exam_id)

        q_body = request.POST.get('newQ_body')
        op1 = request.POST.get('newQ_option1')
        op2 = request.POST.get('newQ_option2')
        op3 = request.POST.get('newQ_option3')
        op4 = request.POST.get('newQ_option4')
        correct_ans = request.POST.get('newQ_correct_ans')

        Question.objects.get_or_create(exam=exam,
                                       body=q_body,
                                       op1=op1,
                                       op2=op2,
                                       op3=op3,
                                       op4=op4,
                                       correct_ans=correct_ans)

        messages.success(request, "Question added successfully")
        return redirect("../")


def edit_exam(request, exam_id):

    form = EditExamForm()

    exam = Exam.objects.get(id=exam_id)

    form.initial['exam_name'] = exam.exam_name
    form.initial['category'] = exam.category

    data = {
        'form': form,
        'exam_id': exam_id,
    }

    return render(request, 'main_app/edit_exam.html', data)


def do_edit_exam(request, exam_id):

    if request.method == 'POST':
        exam = Exam.objects.get(id=exam_id)

        name = request.POST.get('exam_name')
        category = request.POST.get('category')

        list = Exam.objects.filter(examiner=request.user.myuser).exclude(id=exam_id)
        found_exam_with_same_name = False

        for item in list:
            if item.exam_name == name:
                found_exam_with_same_name = True

        if found_exam_with_same_name:
            messages.error(request, "The new exam name contradicts other exam name")
            return redirect("main:edit_exam", exam_id)

        else:
            exam.exam_name = name
            exam.category = category
            exam.save()

            messages.success(request, "The exam updated successfully")
            return redirect("main:all_exams")


def manage_questions(request, exam_id):

    exam = Exam.objects.get(id=exam_id)
    exam_name = exam.exam_name
    exam_category = exam.category

    questions = Question.objects.filter(exam=exam)

    data = {
        'exam_id': exam_id,
        'exam_name': exam_name,
        'exam_category': exam_category,
        'questions': questions
    }
    return render(request, 'main_app/manage_questions.html', data)


def show_exam(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    exam_name = exam.exam_name
    exam_category = exam.category

    questions = Question.objects.filter(exam=exam)
    questions_count = len(questions)

    data = {
        'exam_id': exam_id,
        'exam_name': exam_name,
        'exam_category': exam_category,
        'questions': questions,
        'questions_count': questions_count
    }

    return render(request, 'main_app/show_exam.html', data)


def do_exam(request, exam_id):

    if request.method == 'POST':
        exam = Exam.objects.get(id=exam_id)
        exam_name = exam.exam_name
        exam_category = exam.category

        questions = Question.objects.filter(exam=exam)
        questions_count = len(questions)

    data = {
        'exam_id': exam_id,
        'std_id': request.user.id,
        'exam_name': exam_name,
        'exam_category': exam_category,
        'questions': questions,
        'questions_count': questions_count
    }

    return render(request, 'main_app/do_exam.html', data)


def update_question(request, exam_id, question_id):
    if request.method == 'POST':

        question = Question.objects.get(id=question_id)

        q_body = request.POST.get(f'question-{question.id}-body')
        op1 = request.POST.get(f'question-{question.id}-option-1')
        op2 = request.POST.get(f'question-{question.id}-option-2')
        op3 = request.POST.get(f'question-{question.id}-option-3')
        op4 = request.POST.get(f'question-{question.id}-option-4')
        correct_ans = request.POST.get(f'question-{question.id}-correctA')

        question.body = q_body
        question.op1 = op1
        question.op2 = op2
        question.op3 = op3
        question.op4 = op4
        question.correct_ans = correct_ans

        question.save()
        messages.success(request, "Question updated successfully")
        return redirect('main:manage_questions', exam_id)


def delete_question(request, exam_id, question_id):

    question = get_object_or_404(Question, id=question_id)
    question.delete()

    messages.success(request, 'Question deleted successfully')
    return redirect('main:manage_questions', exam_id)


def delete_exam(request, exam_id):

    exam = get_object_or_404(Exam, id=exam_id)
    exam.delete()

    messages.success(request, 'Exam deleted successfully')
    return redirect('main:all_exams')


# Not completed:


def submit_exam(request, exam_id, std_id):
    return HttpResponse("<h2>YESSS !!</h2>")


def submit_exam2(request):
    if request.method == 'POST':

        return HttpResponse("<h2>OHH YESSSSS , with POST  !!</h2>")

    return HttpResponse("<h2>OHH YESSSSS !!</h2>")
