from django.shortcuts import render
from django.http import request


# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def course(request):
    return render(request,'course.html')
def detail(request):
    return render(request,'detail.html')
