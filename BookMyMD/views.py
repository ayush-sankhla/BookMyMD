from django.shortcuts import render
from django.http import request
from django.contrib.auth.decorators import login_required


def home(request) :
    return render(request, 'home.html')

def about_us (request) :
    return render (request, 'about_us.html')

def contact (request):
    return render (request, 'contact_us.html')