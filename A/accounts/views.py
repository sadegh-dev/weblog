from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserLoginForm

def user_login(request):
    form = UserLoginForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)
