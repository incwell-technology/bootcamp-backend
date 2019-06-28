from django.contrib import admin
from certificate import models as certificate_models


@admin.register(certificate_models.Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('full_name','verification','trainer')
