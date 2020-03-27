from __future__ import unicode_literals
from django.http import HttpResponse, Http404, FileResponse
from .models import Exams, Documents, Slides
from django.shortcuts import render
import os

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

def slides_list(request):
	latest_list = Slides.objects.all()
	context = {'latest_list':latest_list}
	return render(request, 'post/slides.html', context)

def slide_detail(request, id):
	slide = Slides.objects.get(id = id)
	directory = slide.source
	details = []
	for (path, dirnames, filenames) in os.walk(directory):

		for i in filenames:
			list_ = []
			list_.append(path + "/" + i)
			list_.append(i[0:len(i) - 4])
			details.append(tuple(list_))

	return render(request, 'post/slide_detail.html', {'slides':details})
