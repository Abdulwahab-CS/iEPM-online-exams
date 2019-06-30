
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ExaminerCreationForm, StudentCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def home(request):
    return HttpResponse("<h2>Woooow, You are playing with URLs ..</h2>")


def examiner_sign_up(request):
    if request.method == 'POST':
        form = ExaminerCreationForm(request.POST)

        if form.is_valid():

            # make the 'is_examiner flag' is checked !!
            form.save()

            return redirect("/main/")
    else:
        form = UserCreationForm()

    data = {
        'form': form
    }
    return render(request, 'users/examiner_sign_up.html', data)



# def examiner_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request.POST)
#         print(f"\n\n ------> Yes1 \n\n")
#
#         if form.is_valid():
#
#             print(f"\n\n ------> Yes2 \n\n")
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             print(f"\n\n ------> username = {username}\npasswrod = {password} \n\n")
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 redirect('/main/')
#     else:
#         form = AuthenticationForm()
#
#     data = {
#         'form': form
#     }
#     return render(request, 'users/examiner_login.html', data)
