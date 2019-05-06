from django.shortcuts import render
from syllabus import models as syllabus_models
from bootcamp import models as bootcamp_models


def index(request):
    return render(request, "bootcamp/index.html")

def courses(request):
    context = {}
    courses_list = []
    courses = syllabus_models.Course.objects.all()
    for course in courses:
        try:
            image_url = course.image.url.split('/static/')[1]
        except Exception as e:
            print(e)
        courses_list.append({
            'name':course.name,
            'image':image_url,
            'description':course.description,
            'start_time':course.startTime,
            'end_time':course.endTime
        })
    context.update({'courses':courses_list})
    return render(request, "bootcamp/courses.html",context=context)


def mentors(request):
    context = {}
    mentors_list = []
    mentors = bootcamp_models.Mentor.objects.all()
    for mentor in mentors:
        try:
            image_url = mentor.photo.url.split('/static/')[1]
        except Exception as e:
            print(e)
        mentors_list.append({
            'id':mentor.id,
            'firstName':mentor.firstName,
            'summary':mentor.summary,
            'lastName':mentor.lastName,
            'image':image_url,
            'designation': mentor.designation,
            'facebook':mentor.facebookUsername,
            'medium':mentor.mediumUsername,
            'twitter':mentor.twitterUsername,
            'github':mentor.githubUsername,
            'linkedIn':mentor.linkedinUsername,
            'skills':mentor.skill.all()
        })
    context.update({'mentors':mentors_list})
    return render(request, "bootcamp/mentors.html",context=context)