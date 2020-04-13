from __future__ import unicode_literals
from django.http import HttpResponse, Http404, FileResponse
from .models import Exams, Documents, Slides, UploadDocuments, UploadExams
from django.shortcuts import render, redirect
from .filters import SlidesFilter, ExamsFilter, DocumentsFilter
from .forms import DocumentForm, ExamForm
from .documents import updateDocuments
from .exams import updateExams
import os

def base(request):
	return render(request, 'post/base.html')

def exams(request):
	query = Exams.objects.all()
	exams_filter = ExamsFilter(request.GET, queryset=query)
	context = {
		'form': exams_filter.form,
		'exams': exams_filter.qs
	}
	return render(request, 'post/exams.html', context)

def exam_detail(request, id):
	try:
		exam = Exams.objects.get(id = id)
	except Exams.DoesNotExist:
		raise Http404("Exam does not exist")
	return render(request, 'post/exam_detail.html', {'exam': exam})

def exam_upload(request):
	if request.method == 'POST':
		form = ExamForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			exam_auto_update()
			updateExams()
			return redirect('home')
	else:
		form = ExamForm()
	return render(request, 'post/upload_exam.html', {'form': form})

def exam_auto_update():
	query = [UploadExams.objects.all()]
	lastest = query[0][len(query[0]) - 1]
	print(lastest.name)
	filepath = str(lastest.exam)
	path = r"D:/Python/Project1/Source/" + filepath
	path_ = r"D:/Python/Project1/Source/Examination/" + lastest.name + ' - ' + lastest.teacher + '.' + filepath[-3:len(filepath)]
	os.rename(path, path_)

def slides(request):
	query = Slides.objects.all()
	slides_filter = SlidesFilter(request.GET, queryset=query)
	context = {
		'form': slides_filter.form,
		'slides': slides_filter.qs
	}
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

def documents(request):
	query = Documents.objects.all()
	exams_filter = DocumentsFilter(request.GET, queryset=query)
	context = {
		'form': exams_filter.form,
		'documents': exams_filter.qs
	}
	return render(request, 'post/documents.html', context)

def document_detail(request, id):
	try:
		doc = Documents.objects.get(id = id)
	except Documents.DoesNotExist:
		raise Http404("Exam does not exist")
	return render(request, 'post/document_detail.html', {'document': doc})

def document_upload(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			document_auto_update()
			updateDocuments()
			return redirect('home')
	else:
		form = DocumentForm()
	return render(request, 'post/upload_document.html', {'form': form})

def document_auto_update():
	query = [UploadDocuments.objects.all()]
	lastest = query[0][len(query[0]) - 1]
	filepath = str(lastest.document)
	path = r"D:/Python/Project1/Source/" + filepath
	path_ = r"D:/Python/Project1/Source/Documents/" + lastest.name + '.' + filepath[-3:len(filepath)]
	os.rename(path, path_)



# def exams_list(request): #old version
# 	latest_list = Exams.objects.all()
# 	context = {'latest_list' : latest_list}
# 	return render(request, 'post/exams.html', context)

# def documents_list(request): #old version
# 	latest_list = Documents.objects.all()
# 	context = {'latest_list' : latest_list}
# 	return render(request, 'post/documents.html', context)

# def slides_list(request): #old version
# 	latest_list = Slides.objects.all()
# 	context = {'latest_list':latest_list}
# 	return render(request, 'post/slides_oldversion.html', context)