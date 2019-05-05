from django.shortcuts import render
from syllabus import models as syllabus_models

# Create your views here.

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
