from django.contrib import admin
from syllabus import models as syllabus_models


@admin.register(syllabus_models.Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('link', 'link_for')


@admin.register(syllabus_models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','start_time','end_time')


