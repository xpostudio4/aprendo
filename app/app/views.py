from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render

def home(request):
        return render(request, 'index.html')

def schedule(request):
        return render(request, 'programa.html')

def speakers(request):
        return render(request, 'charlistas.html')