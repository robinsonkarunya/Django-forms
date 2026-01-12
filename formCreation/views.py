from django.http import HttpResponse
from django.shortcuts import render
from .forms import InuputForm

def home_view(request):
    context = {}
    context['form'] = InuputForm()
    return render(request,"home.html",context)

def hello_geeks(request):
    return HttpResponse("Hello Geeks")