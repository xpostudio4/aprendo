import json
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
		return render(request, 'charlistas.html')

def workshops(request):
		return render(request, 'talleres.html')

def sponsors(request):
		return render(request, 'patrocinadores.html')

@require_POST
def attendee_form(request):
	form = AttendeeForm(request.POST)
	if form.is_valid:
		f = form.save()
		return HttpResponse(json.dumps({'save' : 'true'}), content_type='application/json')
	return HttpResponseNotFound('Error')