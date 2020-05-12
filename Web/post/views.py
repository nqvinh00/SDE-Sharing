from __future__ import unicode_literals
from django.http import HttpResponse, Http404, FileResponse
from .models import Exams, Documents, Slides, UploadDocuments, UploadExams, UploadSlides
from django.shortcuts import render, redirect
from .filters import SlidesFilter, ExamsFilter, DocumentsFilter
from .forms import DocumentForm, ExamForm, SlidesForm
from .documents import updateDocuments
from .exams import updateExams
from .slides import updateSlides, getDuplicate
import os, mimetypes, shutil

def base(request):
	return render(request, 'post/base.html')

def index(request):
	return render(request, 'post/index.html')

def exam(request):
	query = Exams.objects.all()
	exams_filter = ExamsFilter(request.GET, queryset=query)
	context = {
		'form': exams_filter.form,
		'exams': exams_filter.qs
	}
	return render(request, 'post/exam.html', context)

def slide(request):
	query = Slides.objects.all()
	slides_filter = SlidesFilter(request.GET, queryset=query)
	context = {
		'form': slides_filter.form,
		'slides': slides_filter.qs
	}
	return render(request, 'post/slide.html', context)

def document(request):
	query = Documents.objects.all()
	exams_filter = DocumentsFilter(request.GET, queryset=query)
	context = {
		'form': exams_filter.form,
		'documents': exams_filter.qs
	}
	return render(request, 'post/document.html', context)

def slide_upload_(request):
	if request.method == 'POST':
		form = SlidesForm(request.POST, request.FILES)
		files = request.FILES.getlist('slides')
		if form.is_valid():
			os.makedirs("D:/Python/Project1/Source/Slides/New folder")
			# os.makedirs("/home/nqvinh00/Project1/Source/Slides/New folder")
			for file in files:
				handle_uploaded_file(file)
			form.save()
			slide_auto_update()
			updateSlides()
			return redirect('home')
		print(form.fields.slides)
	else:
		form = SlidesForm()
	return render(request, 'post/slide_upload.html', {'form': form})

def exam_upload_(request):
	if request.method == 'POST':
		form = ExamForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			exam_auto_update()
			updateExams()
			return redirect('home')
	else:
		form = ExamForm()
	return render(request, 'post/exam_upload.html', {'form': form})

def document_upload_(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			document_auto_update()
			updateDocuments()
			return redirect('home')
	else:
		form = DocumentForm()
	return render(request, 'post/document_upload.html', {'form': form})

def about(request):
	return render(request, 'post/about.html')

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
	path_ = r"D:/Python/Project1/Source/Examination/" + lastest.exam_id + ' - ' + lastest.name + ' - ' + lastest.teacher + '.' + filepath[-3:len(filepath)]
	# path = r"/home/nqvinh00/Project1/Source/" + filepath
	# path_ = r"/home/nqvinh00/Project1/Source/Examination/" + lastest.exam_id + ' - ' + lastest.name + ' - ' + lastest.teacher + '.' + filepath[-3:len(filepath)]
	os.rename(path, path_)

def exam_download(request, id):
	try:
		exam = Exams.objects.get(id=id)
		file = open(exam.source, 'rb')
		mimetype, i = mimetypes.guess_type(exam.source)
		response = HttpResponse(file, content_type=mimetype)
		response['Content-Disposition'] = "attachment; filename = %s" % exam.source
		return response
	except Exams.DoesNotExist:
		raise Http404("File does not exist")

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

def slide_upload(request):
	if request.method == 'POST':
		form = SlidesForm(request.POST, request.FILES)
		files = request.FILES.getlist('slides')
		if form.is_valid():
			os.makedirs("D:/Python/Project1/Source/Slides/New folder")
			# os.makedirs("/home/nqvinh00/Project1/Source/Slides/New folder")
			for file in files:
				handle_uploaded_file(file)
			form.save()
			slide_auto_update()
			updateSlides()
			return redirect('home')
		print(form.fields.slides)
	else:
		form = SlidesForm()
	return render(request, 'post/upload_slide.html', {'form': form})

def handle_uploaded_file(file):
	with open('D:/Python/Project1/Source/Slides/New folder/' + file.name, 'wb') as destination:
	# with open('/home/nqvinh00/Project1/Source/Slides/New folder/' + file.name, 'wb') as destination:
		for chunk in file.chunks():
			destination.write(chunk)

def slide_auto_update():
	query = [UploadSlides.objects.all()]
	lastest = query[0][len(query[0]) - 1]
	path = r"D:/Python/Project1/Source/Slides/New folder"
	path_ = r"D:/Python/Project1/Source/Slides/" + lastest.slide_id + ' - ' + lastest.name + ' - ' + lastest.teacher
	# path = r"/home/nqvinh00/Project1/Source/Slides/New folder"
	# path_ = r"/home/nqvinh00/Project1/Source/Slides/" + lastest.slide_id + ' - ' + lastest.name + ' - ' + lastest.teacher
	os.rename(path, path_)
	os.remove(path_ + getDuplicate())

def slide_download(request, id):
	try:
		slide = Slides.objects.get(id=id)
		file_name = slide.slide_id + ' - ' + slide.name + ' - ' + slide.teacher
		path = 'D:/Python/Project1/Source/Slides/'
		# path = '/home/nqvinh00/Project1/Source/Slides/'
		shutil.make_archive(path + file_name, 'zip', slide.source)
		file = open(path + file_name + '.zip', 'rb')
		response = HttpResponse(file, content_type='application.zip')
		response['Content-Disposition'] = "attachment; filename = %s" % file_name
		return response
	except Documents.DoesNotExist:
		raise Http404("File does not exist")
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
	# path = r"/home/nqvinh00/Project1/Source/" + filepath
	# path_ = r"/home/nqvinh00/Project1/Source/Documents/" + lastest.name + '.' + filepath[-3:len(filepath)]
	os.rename(path, path_)

def document_download(request, id):
	try:
		document = Documents.objects.get(id=id)
		file = open(document.source, 'rb')
		mimetype, i = mimetypes.guess_type(document.source)
		response = HttpResponse(file, content_type=mimetype)
		response['Content-Disposition'] = "attachment; filename = %s" % document.source
		return response
	except Documents.DoesNotExist:
		raise Http404("File does not exist")

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