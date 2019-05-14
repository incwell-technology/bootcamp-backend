from django.contrib.auth.models import User
from visitor import models as visitor_models
from syllabus import models as syllabus_models
import uuid

def enroll_student(request):
    try:
        course = syllabus_models.Course.objects.filter(id=request.POST['courses'])
        try:
            gender = True
            full_name = request.POST['first_name']+" "+request.POST['middle_name']+" "+request.POST['last_name']
            if request.POST.get('gender') == "0":
                gender = False
            enroll = visitor_models.StudentEnroll.objects.create(firstName=request.POST['first_name'],middleName=request.POST['middle_name'],lastName=request.POST['last_name'], fullName=full_name,email=request.POST['email'],
                    education=request.POST['education'], gender = gender,phone=request.POST['phone'], gitLink=request.POST['git_link'])
            for enr_course in course:
                enroll.course.add(enr_course)
            if enroll:
                return True
            return False
        except Exception as e:
            print(e)
            return False
    except syllabus_models.Course.DoesNotExist:
        return False


def  validate_contact(request):
    err = []
    if request.POST['full_name'] == "":
        err.append('Full Name field is required.')
    if request.POST.get('email') == "":
        err.append('Email field is required.')
    if request.POST.get('skype_id') == "":
        err.append('Skype field is required.')

    return err