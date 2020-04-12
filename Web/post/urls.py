from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
	path('', views.base, name = 'home'),
	path('exams/', views.exams, name = 'exams'),
	path('exams/<int:id>/', views.exam_detail),
	path('documents/', views.documents, name = 'documents'),
	path('documents/<int:id>/', views.document_detail),
	path('slides/', views.slides, name = 'slides'),
	path('slides/<int:id>/', views.slide_detail),
	path('upload_document/', views.document_upload, name = 'upload_document'),
	path('upload_exam/', views.exam_upload, name = 'upload_exam'),
]