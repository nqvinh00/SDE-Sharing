from django import forms
from .models import UploadDocuments, UploadExams, UploadSlides

class DocumentForm(forms.ModelForm):
	class Meta:
		model = UploadDocuments
		fields = ('name', 'document', )
		labels = {'name': 'Tên sách, tài liệu', 'document':'File'}
		help_texts = {'name':'Vui lòng điền đầy đủ tên sách',}

class ExamForm(forms.ModelForm):
	class Meta:
		model = UploadExams
		fields = ('name', 'exam_id', 'teacher', 'exam')
		labels = {'name': 'Tên môn', 'exam':'File', 'exam_id':'Mã môn', 'teacher':'Tên giảng viên'}
		help_texts = {'name':'Vui lòng điền đầy đủ thông tin', 'exam':'Tải lên file của bạn', 
					'exam_id':'Vui lòng điền đầy đủ thông tin', 'teacher':'Vui lòng điền đầy đủ thông tin'}

class SlidesForm(forms.ModelForm):
	class Meta:
		model = UploadSlides
		fields = ('name', 'slide_id', 'teacher', 'slides')
		labels = {'name': 'Tên môn', 'slides':'Files', 'teacher':'Tên giảng viên', 'slide_id':'Mã môn'}
		help_texts = {'name':'Vui lòng điền đầy đủ thông tin', 'slides':'Tải lên các file của bạn', 
					'teacher':'Vui lòng điền đầy đủ thông tin', 'slide_id':'Vui lòng điền đầy đủ thông tin'}
		widgets = {'slides': forms.FileInput(attrs={'multiple':True})}