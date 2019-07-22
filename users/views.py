
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import MyUserCreationForm
from .models import MyUser
from main_app.models import Exam
from django.shortcuts import get_object_or_404
from django.contrib import messages


def home(request):
    my_user = MyUser.objects.get(user=request.user)
    if my_user.is_examiner:
        return HttpResponseRedirect("/users/examiners/" + my_user.slug + "/")
    elif my_user.is_student:
        return HttpResponseRedirect("/users/students/" + my_user.slug + "/")


def examiner_sign_up(request):

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            MyUser.objects.get_or_create(user=user, is_examiner=True)

            messages.success(request, f"Your account created successfully")
            return redirect('users:login')

    else:
        form = MyUserCreationForm()

    data = {
        'form': form
    }
    return render(request, 'users/examiners/examiner_sign_up.html', data)


def student_sign_up(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            MyUser.objects.get_or_create(user=user, is_student=True)

            messages.success(request, f"Your account created successfully")
            return redirect('users:login')

    else:
        form = MyUserCreationForm()

    data = {
        'form': form
    }
    return render(request, 'users/students/student_sign_up.html', data)


# the reason behind using the name 'the_login' , 'the_logout' , is to not conflict with the built in login function
def the_login(request):

    form = AuthenticationForm()

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome ( {username} )")
            return redirect('users:home')

        else:
            messages.error(request, f"Invalid Username or Password !!")

    data = {
        'form': form
    }
    return render(request, 'users/login.html', data)


def the_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('main:home')


def examiner_profile(request, slug):

    if request.method == 'POST':
        profile = get_object_or_404(MyUser, slug=slug)

        if profile.is_valid():
            redirect('users/examiners/examiner_profile.html')

    else:
        profile = AuthenticationForm()

    profile = get_object_or_404(MyUser, slug=slug)
    data = {
        'profile': profile
    }
    return render(request, 'users/examiners/examiner_profile.html', data)


def student_profile(request, slug):

    if request.method == 'POST':
        profile = get_object_or_404(MyUser, slug=slug)

        if profile.is_valid():
            redirect('users/students/student_profile.html')

    else:
        profile = AuthenticationForm()

    profile = get_object_or_404(MyUser, slug=slug)

    exams = Exam.objects.filter(is_published=True)

    data = {
        'profile': profile,
        'exams': exams
    }
    return render(request, 'users/students/student_profile.html', data)


