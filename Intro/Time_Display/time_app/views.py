from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now()
    context = {
        'time': datetime.strftime(now,"%H:%M %p %m-%d-%Y")
    }
    return render(request, 'index.html',context)