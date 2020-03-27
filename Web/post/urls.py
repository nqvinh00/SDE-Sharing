from django.urls import path
from django.conf.urls import url
from .views import exams_list, exam_detail, base, slides_list, slide_detail
urlpatterns = [
	path('', base),
	path('exams/', exams_list),
	path('exams/<int:id>/', exam_detail),
	path('slides/', slides_list),
	path('slides/<int:id>/', slide_detail),
]