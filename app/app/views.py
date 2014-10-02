from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render

def home(request):
        return render(request, 'index.html')

def schedule(request):
        return render(request, 'programa.html')
