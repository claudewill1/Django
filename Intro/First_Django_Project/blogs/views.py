from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse

# Create your views here.
def root_method(request):
    return redirect('/blogs')
def index(request):
    return HttpResponse('placeholder to later display a list of all blogs')
def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog')
def create(request):
    return redirect('/')
def show(request,number):
    return HttpResponse(f'placeholder to display blog number {number}')
def delete(request,number):
    return redirect('/blogs')
def edit(request,number):
    return HttpResponse(f'placeholder to edit blog {number}')
def json(request):
    return JsonResponse({'title':'My First Blog','content':'Lorem, ipsum dolor sit amet consectetur adipisicing elite.'})
