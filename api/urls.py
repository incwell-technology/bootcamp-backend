from rest_framework import routers
from syllabus.api import CourseViewSet
from visitor.api import EnrollViewSet, TalkViewSet
from bootcamp.api import CompanyViewSet, MentorViewSet, ContentViewSet

router = routers.DefaultRouter()
router.register('api/courses', CourseViewSet, 'courses')
router.register('api/enroll', EnrollViewSet, 'enroll')
router.register('api/company', CompanyViewSet, 'company')
router.register('api/mentors', MentorViewSet, 'mentors')
router.register('api/contents', ContentViewSet, 'contents')
router.register('api/talk-to-advisor', TalkViewSet, 'talk')

urlpatterns = router.urls