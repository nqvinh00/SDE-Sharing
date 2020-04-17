from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path('', views.base, name = 'home'),
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
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)