from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from datetime import date

TODAY = date.today

def home(request):
    return render(request, 'home/home.html', {"today": TODAY})

@login_required(login_url='/admin/login/')
def authenticated(request):
    return render(request, 'home/authenticated.html', {"today": TODAY})
