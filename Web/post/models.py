from django.db import models
from django.db.models import Q

class Exams(models.Model):
	exam_id = models.CharField(max_length = 15)
	name = models.CharField(max_length = 100)
	teacher = models.CharField(max_length = 200)
	# time = models.CharField(max_length = 50)
	source = models.CharField(max_length = 200)

	def __str__(self):
		return self.name

	class Meta:
		default_related_name = 'exams'

class Documents(models.Model):
	name = models.CharField(max_length = 200)
	source = models.CharField(max_length = 200)

	def __str__(self):
		return self.name

	class Meta:
		default_related_name = 'documents'

class Slides(models.Model):
	slide_id = models.CharField(max_length = 15)
	name = models.CharField(max_length = 100)
	teacher = models.CharField(max_length = 200)
	# time = models.CharField(max_length = 50)
	source = models.CharField(max_length = 200)

	def __str__(self):
		return self.name

	class Meta:
		default_related_name = 'slides'

class UploadDocuments(models.Model):
	document = models.FileField(upload_to='Documents/', unique=True)
	date = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length = 200, default="")
	description = models.CharField(max_length=255, blank=True)

class UploadExams(models.Model):
	exam = models.FileField(upload_to='Examination/', unique=True)
	date = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length = 200, default="")
	teacher = models.CharField(max_length = 200)
	exam_id = models.CharField(max_length = 15)

class UploadSlides(models.Model):
	slide_id = models.CharField(max_length = 15)
	date = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length = 100, unique=True, default="")
	teacher = models.CharField(max_length = 200)
	slides = models.FileField(upload_to='Slides/New folder')