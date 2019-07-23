from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import AddExamForm, EditExamForm
from .models import Exam, Question, TakenExam
from users.models import MyUser
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

            # check if found exam with same name and category
            temp = Exam.objects.filter(
                exam_name__iexact=exam_name,
                category__iexact=category
            )

            if temp:
                messages.error(request, "Found exam with same name and category")
                return redirect('main:add_exam')

            else:
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


def add_question(request, exam_id):
    if request.method == 'POST':

        exam = Exam.objects.get(id=exam_id)

        q_body = request.POST.get('newQ_body')
        op1 = request.POST.get('newQ_option1')
        op2 = request.POST.get('newQ_option2')
        op3 = request.POST.get('newQ_option3')
        op4 = request.POST.get('newQ_option4')
        correct_ans = request.POST.get('newQ_correctA')

        Question.objects.get_or_create(exam=exam,
                                       body=q_body,
                                       op1=op1,
                                       op2=op2,
                                       op3=op3,
                                       op4=op4,
                                       correct_ans=correct_ans)
        messages.success(request, "Question added successfully")
        return HttpResponse(1)

    else:
        return HttpResponse(0)


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

        # if nothing is changed
        if exam.exam_name == name and exam.category == category:
            return redirect("main:all_exams")

        # check if found exam with same name and category
        exams = Exam.objects.filter(examiner=request.user.myuser).exclude(id=exam_id)
        temp = exams.filter(exam_name__iexact=name, category__iexact=category)

        if temp:
            messages.error(request, "Found exam with same name and category")
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

        # check if the student take this exam before or not
        temp = TakenExam.objects.filter(exam=exam, student=request.user.myuser)

        if temp:
            messages.error(request, f"You have done this exam before !")
            return redirect("users:home")

        else:
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

        q_body = request.POST.get('qBody')
        op1 = request.POST.get('op1')
        op2 = request.POST.get('op2')
        op3 = request.POST.get('op3')
        op4 = request.POST.get('op4')
        correct_ans = request.POST.get('correctA')

        question.body = q_body
        question.op1 = op1
        question.op2 = op2
        question.op3 = op3
        question.op4 = op4
        question.correct_ans = correct_ans

        question.save()
        messages.success(request, "Question updated successfully")

        return HttpResponse(1)
        # return redirect('main:manage_questions', exam_id)

    else:
        return HttpResponse(0)


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


def submit_exam(request):
    if request.method == 'POST':

        exam_id = request.POST.get('examID')
        std_id = request.POST.get('stdID')
        answers = request.POST.get('answers')
        # !!!!! really strange : if I write : -> request.POST['answers'] : produces Internal Server Error (500)

        # get the exam questions to calc scores
        all_questions = Question.objects.filter(exam=exam_id)

        # to make the answers iterable, because now it's one string, so we want to remove the commas
        answers = answers.split(',')

        # calc student score in the exam
        score = 0
        for i in range(len(answers)):
            if int(answers[i]) == int(all_questions[i].correct_ans):
                score += 1

        # get the exam and the student and add the score in the database
        exam = Exam.objects.get(id=exam_id)
        student = request.user.myuser

        TakenExam.objects.get_or_create(student=student, exam=exam, score=score, full_mark=len(all_questions))
        return HttpResponse(1)
    else:
        return HttpResponse(0)


def students_scores(request):

    temp = TakenExam.objects.all()
    results = []
    for t in temp:
        if t.exam.examiner == request.user.myuser:
            results.append(t)

    data = {
        'results': results
    }
    return render(request, 'main_app/students_scores.html', data)


def clear_scores(request):

    # get all the exams that created by this examiner
    exams_to_delete = Exam.objects.filter(examiner=request.user.myuser)

    # delete all scores that related to those exams (clear operation)
    for x in exams_to_delete:
        x.takenexam_set.all().delete()

    '''
        # The NONE efficient way to do (clear operation)
        
        # targeted_exams = Exam.objects.filter(examiner=request.user.myuser)
        # temp = TakenExam.objects.filter(exam=targeted_exams).delete()
        #
        # for t in temp:
        #     if t.exam.examiner == request.user.myuser:
        #         t.delete()
    '''

    messages.success(request, "All scores cleared successfully")
    return redirect("users:home")


def publish_exam(request, exam_id):

    exam = get_object_or_404(Exam, id=exam_id)
    exam.is_published = True
    exam.save()

    messages.success(request, 'Exam published successfully')
    return redirect('main:all_exams')


def un_publish_exam(request, exam_id):

    exam = get_object_or_404(Exam, id=exam_id)
    exam.is_published = False
    exam.save()

    messages.success(request, 'Exam Un-published successfully')
    return redirect('main:all_exams')

