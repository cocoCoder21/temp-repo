from django.shortcuts import render, redirect
from fitapp.forms import UserInfoForm, UserProfileForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from fitapp.models import UserModels

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def us(request):
    return render(request, 'us.html')

def user_signup(request):
    if request.method == 'POST':
        userinfo = UserInfoForm(request.POST)
        userprofile = UserProfileForm(request.POST)
        if userinfo.is_valid() and userprofile.is_valid():
            user = userinfo.save()
            user.set_password(user.password)
            user.save()
            profile = userprofile.save(commit=False)

            profile.user = user

            profile.save()
        else:
            print(userinfo.errors, userprofile.errors)
    else:
        userinfo = UserInfoForm()
        userprofile = UserProfileForm()
    return render(request, 'signup.html', {'form1':userinfo, 'form2':userprofile})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user and user.is_active:
            login(request, user)
            return redirect('user_home.html', username=user.username)
    return render(request, 'login.html')


def user_logout(request):
    pass

def user_page(request, username):
    user = UserModels.objects.all()
    print(username)
    # for acc in len(user):
    #     if user[acc].user.username == username:
    return render(request, 'user_home.html')
