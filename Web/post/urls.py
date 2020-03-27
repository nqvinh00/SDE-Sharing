from django.urls import path
from django.conf.urls import url
from .views import exams_list, exam_detail, base
urlpatterns = [
	path('', base),
	path('exams/', exams_list),
	path('<int:id>/', exam_detail),
]