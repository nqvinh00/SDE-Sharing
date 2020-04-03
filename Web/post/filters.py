from django import forms
import django_filters
from .models import Exams, Documents, Slides

class SlidesFilter(django_filters.FilterSet):
	slide_id = django_filters.CharFilter(lookup_expr='icontains')
	name = django_filters.CharFilter(lookup_expr='icontains')
	teacher = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = Slides
		fields = ('name','slide_id', 'teacher')

class ExamsFilter(django_filters.FilterSet):
	exam_id = django_filters.CharFilter(lookup_expr='icontains')
	name = django_filters.CharFilter(lookup_expr='icontains')
	teacher = django_filters.CharFilter(lookup_expr='icontains')

	class Meta:
		model = Exams
		fields = ('name','exam_id', 'teacher')

class DocumentsFilter(django_filters.FilterSet):
	name = django_filters.CharFilter(lookup_expr='icontains')

	class Meta:
		model = Documents
		fields = ('name',)