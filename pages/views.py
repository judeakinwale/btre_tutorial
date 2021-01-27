from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  # return HttpResponse('hello world')
  return render(request, template_name="pages/index.html", context={})

def about(request):
  # return HttpResponse('hello world')
  return render(request, template_name="pages/about.html", context={})
  