from django.urls import path, include
from bootcamp import views as bootcamp_views


urlpatterns = [
    path('', bootcamp_views.index, name="index"),
    path('courses', include('syllabus.urls')),
    path('mentors', bootcamp_views.mentors, name="mentors")
]
