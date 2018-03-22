from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template = 'blog/index.html'
    return render(request, template, {})

# Create your views here.
