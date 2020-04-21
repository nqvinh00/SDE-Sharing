from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path('home/', views.base, name = 'home'),
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('exam/', views.exam, name='exam'),
	path('slide/', views.slide, name='slide'),
	path('document/', views.document, name='document'),
	path('slide_upload/', views.slide_upload_, name = 'slide_upload'),
	path('exam_upload/', views.exam_upload_, name = 'exam_upload'),
	path('document_upload/', views.document_upload_, name = 'document_upload'),
	path('exams/', views.exams, name = 'exams'),
	path('exams/<int:id>/', views.exam_detail),
	path('upload_exam/', views.exam_upload, name = 'upload_exam'),
	path('exams/download/<int:id>/', views.exam_download),
	path('documents/', views.documents, name = 'documents'),
	path('documents/<int:id>/', views.document_detail),
	path('upload_document/', views.document_upload, name = 'upload_document'),
	path('documents/download/<int:id>/', views.document_download),
	path('slides/', views.slides, name = 'slides'),
	path('slides/<int:id>/', views.slide_detail),
	path('upload_slide/', views.slide_upload, name = 'upload_slide'),
	path('slides/download/<int:id>/', views.slide_download),
]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)