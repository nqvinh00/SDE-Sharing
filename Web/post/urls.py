from django.urls import path
from django.conf.urls import url
from .views import exams_list, exam_detail, base, slides_list
urlpatterns = [
	path('', base),
	path('exams/', exams_list),
	path('exams/<int:id>/', exam_detail),
	path('slides/', slides_list),
]