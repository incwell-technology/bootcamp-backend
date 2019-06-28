from django.urls import path, include
from bootcamp import views as bootcamp_views


urlpatterns = [
    path('', bootcamp_views.index, name="index"),
    path('courses', include('syllabus.urls')),
    path('mentors', bootcamp_views.mentors, name="mentors"),
    path('enroll', bootcamp_views.enroll, name="enroll"),
    path('about', bootcamp_views.about, name="about"),
    path('contact', bootcamp_views.contact, name="contact"),
    path('scholarship', bootcamp_views.scholarship, name="scholarship"),
    path('apply-scholarship', bootcamp_views.apply_scholarship, name="apply-scholarship"),
    path('events', bootcamp_views.events, name="events")
]
