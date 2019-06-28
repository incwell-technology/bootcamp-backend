from django.contrib import admin
from event import models as event_models


@admin.register(event_models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title','venue','date')


@admin.register(event_models.Main_Event)
class Main_EventAdmin(admin.ModelAdmin):
    list_display = ('title','venue','date')