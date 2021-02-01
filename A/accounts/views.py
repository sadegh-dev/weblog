from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password= form.cleaned_data['password']
            user = authenticate(request, username= username, password= password)
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully !','success')
                return redirect('blog:all_articles') 
            else :
                messages.error(request, 'wrong yousername or password !','warning')          
    else:
        form = UserLoginForm()
    
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data  #copy all cleaned data
            User.objects.create_user(cd['username'],cd['email'],cd['password'])
            messages.success(request,'you registered successfuly, now log in', 'success')
            return redirect('accounts:user_login')
    else:
        form = UserRegistrationForm()
        context = {'form':form}
        return render(request, 'accounts/register.html', context)


def user_logout(request):
    logout(request)
    messages.success(request,'you logout successfuly', 'success')
    return redirect('blog:all_articles')
