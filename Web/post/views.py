from __future__ import unicode_literals
from django.http import HttpResponse, Http404, FileResponse
from .models import Exams, Documents
from django.shortcuts import render

def base(request):
	return render(request, 'post/base.html')

def exams_list(request):
	latest_list = Exams.objects.all()
	context = {'latest_list' : latest_list}
	return render(request, 'post/exams.html', context)

def exam_detail(request, id):
	try:
		exam = Exams.objects.get(id = id)
	except Exams.DoesNotExist:
		raise Http404("Exam does not exist")
	return render(request, 'post/exam_detail.html', {'exam': exam})