from django.db import models

class Exams(models.Model):
	exam_id = models.CharField(max_length = 15)
	name = models.CharField(max_length = 100)
	teacher = models.CharField(max_length = 200)
	# time = models.CharField(max_length = 50)
	source = models.CharField(max_length = 200)

	def __str__(self):
		return self.name

class Documents(models.Model):
	name = models.CharField(max_length = 200)
	source = models.CharField(max_length = 200)

	def __str__(self):
		return self.name

class Slides(models.Model):
	slide_id = models.CharField(max_length = 15)
	name = models.CharField(max_length = 100)
	teacher = models.CharField(max_length = 200)
	# time = models.CharField(max_length = 50)
	source = models.CharField(max_length = 200)