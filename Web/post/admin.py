from django.contrib import admin

from .models import Slides, Exams, Documents

admin.site.register(Slides)
admin.site.register(Exams)
admin.site.register(Documents)