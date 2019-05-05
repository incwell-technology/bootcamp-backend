from django.urls import path, include
from bootcamp import views as bootcamp_views
from syllabus import views as syllabus_views


urlpatterns = [
    path('', syllabus_views.courses, name="courses")
]
