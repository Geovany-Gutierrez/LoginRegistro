# core/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def signUp(request):
    return render(request, 'core/signUp.html')

def signIn(request):
    return render(request, 'core/signIn.html')
