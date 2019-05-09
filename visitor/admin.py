from django.contrib import admin
from visitor import models as visitor_models


@admin.register(visitor_models.StudentEnroll)
class StudentEnrollAdmin(admin.ModelAdmin):
    list_display = ('fullName','gitLink','phone')

@admin.register(visitor_models.Talk_To_Mentor)
class TalkAdmin(admin.ModelAdmin):
    list_display = ('firstName','lastName','email')
