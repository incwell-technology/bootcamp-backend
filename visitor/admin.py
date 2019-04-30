from django.contrib import admin
from visitor import models as visitor_models


@admin.register(visitor_models.Enroll)
class EnrollAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','git_link')


@admin.register(visitor_models.Talk_To_Mentor)
class TalkAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')

