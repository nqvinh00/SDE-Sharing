from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
	path('', views.base),
	path('exams/', views.exams_list),
	path('exams/<int:id>/', views.exam_detail),
	path('slides/', views.slides_list),
	path('slides/<int:id>/', views.slide_detail),
	path('documents/', views.documents_list),
	path('documents/<int:id>/', views.document_detail),
]