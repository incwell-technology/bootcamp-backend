from django.db import models
from django.utils import timezone
from bootcamp import models as bootcamp_models
from syllabus import models as syllabus_models


class Certificate(models.Model):
    verification = models.CharField(max_length=300, null=False, blank=False, default="0628201901", unique=True)
    pdf = models.FileField(upload_to="bootcamp/static/bootcamp/site-data/certificate-pdf", null=False, blank=False)
    full_name = models.CharField(max_length=500, null=False, blank=False, default="")
    course = models.ForeignKey(syllabus_models.Course, on_delete=models.CASCADE)
    course_duration = models.CharField(max_length=200, null=False, blank=False, default="")
    start_date = models.DateField(null=False, blank=False, default=timezone.now())
    completed_date = models.DateField(null=False, blank=False, default=timezone.now())
    trainer = models.ForeignKey(bootcamp_models.Mentor, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="bootcamp/static/bootcamp/site-data/certificate-photo", null=False, blank=False)

    def __str__(self):
        return self.full_name
        