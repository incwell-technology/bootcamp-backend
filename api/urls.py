from rest_framework import routers
from syllabus.api import CourseViewSet
from visitor import api as visitor_api
from bootcamp.api import CompanyViewSet, MentorViewSet, ContentViewSet

router = routers.DefaultRouter()
router.register('courses', CourseViewSet, 'courses')
router.register('students', visitor_api.StudentViewSet, 'students')
router.register('company', CompanyViewSet, 'company')
router.register('mentors', MentorViewSet, 'mentors')
router.register('contents', ContentViewSet, 'contents')
router.register('talk-to-advisor', visitor_api.TalkViewSet, 'talk')

urlpatterns = router.urls