from rest_framework import routers
from syllabus.api import CourseViewSet
from visitor import api as visitor_api
from bootcamp.api import CompanyViewSet, MentorViewSet, ContentViewSet

router = routers.DefaultRouter()
router.register('api/courses', CourseViewSet, 'courses')
router.register('api/students', visitor_api.StudentViewSet, 'students')
router.register('api/company', CompanyViewSet, 'company')
router.register('api/mentors', MentorViewSet, 'mentors')
router.register('api/contents', ContentViewSet, 'contents')
router.register('api/talk-to-advisor', visitor_api.TalkViewSet, 'talk')

urlpatterns = router.urls