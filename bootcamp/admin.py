from django.contrib import admin
from bootcamp import models as bootcamp_models


admin.site.register(bootcamp_models.Company)
admin.site.register(bootcamp_models.Skill)
admin.site.register(bootcamp_models.Content)


@admin.register(bootcamp_models.Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('firstName','lastName','designation')
