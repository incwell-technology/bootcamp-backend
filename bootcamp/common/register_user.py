from django.contrib.auth.models import User
from visitor import models as visitor_models
from syllabus import models as syllabus_models


def register_django_user(request):
    try:
        counter = 1
        if not User.objects.first():
            counter = 1
        else:
            count = User.objects.last()
            counter = count.id
        username = request.POST['first_name']+" "+request.POST['middle_name']+" "+request.POST['last_name']+str(counter)
        user = User.objects.create(username=username,first_name=request.POST['first_name'],
                                   last_name=request.POST['last_name'], email=request.POST['email'])
        user.save()

        if enroll_student(request, user):
            return True
        else:
            user.delete()
            return False
    except Exception as e:
        print(e)
        return False


def enroll_student(request, user):
    try:
        course = syllabus_models.Course.objects.filter(id=request.POST['courses'])
        try:
            gender = True
            full_name = request.POST['first_name']+" "+request.POST['middle_name']+" "+request.POST['last_name']
            if request.POST.get('gender') == "0":
                gender = False
            enroll = visitor_models.StudentEnroll.objects.create(user=user, full_name=full_name,email=request.POST['email'], middleName=request.POST['middle_name'],
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