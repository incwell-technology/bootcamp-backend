from django.urls import path, include
from bootcamp import views as bootcamp_views


urlpatterns = [
    path('', bootcamp_views.index, name="index"),
    path('courses', include('syllabus.urls')),
    path('mentors', bootcamp_views.mentors, name="mentors"),
    path('enroll', bootcamp_views.enroll, name="enroll"),
    path('talk-to-mentors', bootcamp_views.talk_to_mentors, name="talk-to-mentors"),
    path('about', bootcamp_views.about, name="about")
]
