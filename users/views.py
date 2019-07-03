
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from main_app.models import MyUser

from django.shortcuts import get_object_or_404


def home(request):
    my_user = MyUser.objects.get(user=request.user)
    if my_user.is_examiner:
        return HttpResponseRedirect("/users/examiner/" + my_user.slug + "/")
    elif my_user.is_student:
        return HttpResponseRedirect("/users/student/" + my_user.slug + "/")


def examiner_sign_up(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            MyUser.objects.get_or_create(user=user, is_examiner=True)

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/users')

    else:
        form = UserCreationForm()

    data = {
        'form': form
    }
    return render(request, 'users/examiner_sign_up.html', data)


def student_sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            MyUser.objects.get_or_create(user=user, is_student=True)
            return redirect("/home/")
    else:
        form = UserCreationForm()

    data = {
        'form': form
    }
    return render(request, 'users/student_sign_up.html', data)


def examiner_login(request):
    # if request.method == 'POST':
    #     form = ExaminerLoginForm(request.POST)
    #
    #     if form.is_valid():
    #
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password')
    #
    #         user = authenticate(username=username, passwrod=password)
    #
    #         if user is not None:
    #             login(request, user)
    #             redirect('users:home')
    #
    # else:
    #     form = ExaminerLoginForm()
    #
    # data = {
    #     'form': form
    # }
    # return render(request, 'users/examiner_login.html', data)

    pass


def student_login(request):
    pass


def examiner_profile(request, slug):

    if request.method == 'POST':
        profile = get_object_or_404(MyUser, slug=slug)

        if profile.is_valid():
            redirect('users/examiner_profile.html')

    else:
        profile = AuthenticationForm()

    profile = get_object_or_404(MyUser, slug=slug)
    data = {
        'profile': profile
    }
    return render(request, 'users/examiner_profile.html', data)


def student_profile(request, slug):

    if request.method == 'POST':
        profile = get_object_or_404(MyUser, slug=slug)

        if profile.is_valid():
            redirect('users/student_profile.html')

    else:
        profile = AuthenticationForm()

    profile = get_object_or_404(MyUser, slug=slug)
    data = {
        'profile': profile
    }
    return render(request, 'users/student_profile.html', data)

