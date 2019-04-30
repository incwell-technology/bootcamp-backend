from django.contrib import admin
from visitor import models as visitor_models


@admin.register(visitor_models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('firstName','lastName','email','gitLink')


@admin.register(visitor_models.Talk_To_Mentor)
class TalkAdmin(admin.ModelAdmin):
    list_display = ('firstName','lastName','email')

admin.site.register(visitor_models.Enroll)
