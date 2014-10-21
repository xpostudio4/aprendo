import json
import sys
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.http import require_POST
from attendee.forms import AttendeeForm

def home(request):
		form = AttendeeForm()
		return render(request, 'index.html', {'form': form })

def schedule(request):
		form = AttendeeForm()
		return render(request, 'programa.html', {'form': form })

def speakers(request):
		form = AttendeeForm()
		return render(request, 'charlistas.html', {'form': form })

def workshops(request):
		form = AttendeeForm()
		return render(request, 'talleres.html', {'form': form })

def sponsors(request):
		form = AttendeeForm()
		return render(request, 'colaboradores.html', {'form': form })

def press(request):
		form = AttendeeForm()
		return render(request, 'prensa.html', {'form': form })

@require_POST
def attendee_form(request):
	form = AttendeeForm(request.POST)
	if form.is_valid():
		try: 
			f = form.save()
			return HttpResponse(json.dumps({'save' : 'true'}), content_type='application/json')
		except Exception as x:
			return HttpResponse(x)
	print >>sys.stderr, form.errors
	return HttpResponse(form.errors)