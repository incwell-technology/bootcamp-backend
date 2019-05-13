from django.shortcuts import render, reverse
from syllabus import models as syllabus_models
from bootcamp import models as bootcamp_models
from visitor import models as visitor_models
from django.contrib import messages
from django.http import HttpResponseRedirect
from bootcamp.common import register_user
import re
from django.db.models import Q


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
    mentors_all = get_all_mentors()
    categories = bootcamp_models.MentorCategory.objects.all()
    for mentor in mentors:
        try:
            image_url = mentor.photo.url.split('/static/')[1]
        except Exception as e:
            print(e)
        category_list = []
        for category in mentor.mentorCategory.all():
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
                'category':category,
                'skills':mentor.skill.all()
            })
    context.update({'mentors':mentors_list})
    context.update({'mentors_all':mentors_all})
    context.update({'categories':categories})
    return render(request, "bootcamp/mentors.html",context=context)


def enroll(request):
    context = {}
    courses = syllabus_models.Course.objects.order_by("-id").all()
    context.update({'courses':courses})
    
    if request.method == "POST":
        error = validate_enroll_data(request)

        if error:
            messages.success(request, "Please correct following error.",extra_tags="0")
            context.update({'error':error})    
            context.update({'first_name':request.POST['first_name']})    
            context.update({'middle_name':request.POST['middle_name']})    
            context.update({'last_name':request.POST['last_name']})    
            context.update({'email':request.POST['email']})    
            context.update({'git_link':request.POST['git_link']})    
            context.update({'education':request.POST['education']})    
            context.update({'phone':request.POST['phone']})    
            context.update({'phone':request.POST['phone']})    
            context.update({'gender':request.POST.get('gender')})
            context.update({'course':request.POST.get('course')})
            return render(request, "bootcamp/enroll.html", context=context)
        else:
            try:
                user = register_user.enroll_student(request)
                if user:
                    messages.success(request, "Thank You for Enrolling. We will contact you soon.", extra_tags="1")
                else:
                    messages.success(request, "Sorry. Enroll has not been submitted. Please try again.", extra_tags="0")
                return HttpResponseRedirect(reverse('enroll'))
            except Exception as e:
                print(e)
                messages.success(request, "Sorry. Enroll has not been submitted. Please try again.", extra_tags="0")
                return HttpResponseRedirect(reverse('enroll'))
    else:
        return render(request, "bootcamp/enroll.html", context=context)


def validate_enroll_data(request):
    err = []
    if request.POST['first_name'] == "":
        err.append("First Name field is required.")

    if request.POST['last_name'] == "":
        err.append("Last Name field is required.")

    if request.POST['email'] == "": 
        err.append("Email field is required.")

    if request.POST['phone'] == "":
        err.append("Phone number field is required.")
    
    if request.POST['education'] == "":
        err.append("Education field is required.")

    if request.POST['courses'] is None:
        err.append('Please choose your course to enroll.')

    if request.POST['gender'] is None:
        err.append('Please choose your gender.')

    return err


def talk_to_mentors(request):
    context = {}
    if request.method == "POST":
        error = validate_talk_to_mentors(request)
        if error:
            messages.success(request, "Please correct following error.", extra_tags="0")
            context.update({'error':error})
            context.update({'first_name':request.POST['first_name']})
            context.update({'last_name':request.POST['last_name']})
            context.update({'email':request.POST['email']})
            return render(request, "bootcamp/talk-to-mentors.html", context=context)
        else:
            talk = visitor_models.Talk_To_Mentor.objects.create(firstName=request.POST['first_name'],
            lastName=request.POST['last_name'], email=request.POST['email'])
            if talk:
                messages.success(request, "Thank You. We will contact you soon.", extra_tags="1")
            else:
                messages.success(request, "Sorry. The form was not submit.Please try again.", extra_tags="0")
        return HttpResponseRedirect(reverse('talk-to-mentors'))
    else:
        return render(request, "bootcamp/talk-to-mentors.html")
    

def  validate_talk_to_mentors(request):
    err = []
    if request.POST['first_name'] == "":
        err.append('First Name field is required.')
    if request.POST['last_name'] == "":
        err.append('Last Name field is required.')
    if request.POST['email'] == "":
        err.append('Email field is required.')

    return err


def get_all_mentors():
    mentors = bootcamp_models.Mentor.objects.all()
    mentors_list = []
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
    return mentors_list


def about(request):
    teams = bootcamp_models.Team.objects.all()
    about_content = bootcamp_models.Content.objects.filter(Q(title='About') | Q(title="About Us") | Q(title="about") | Q(title="about us"))
    team_list = []
    for team in teams:
        try:
            image_url = team.image.url.split('/static/')[1]
        except Exception as e:
            print(e)
        team_list.append({
            'id':team.id,
            'firstName':team.firstName,
            'lastName':team.lastName,
            'image':image_url,
            'designation': team.designation,
        })
    context = {}
    context.update({'teams':team_list})
    context.update({'about_content':about_content[0]})
    return render(request, "bootcamp/about.html", context=context)