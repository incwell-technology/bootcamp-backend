from syllabus import models as syllabus_models
from rest_framework import viewsets, permissions
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = syllabus_models.Course.objects.order_by("-id").all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CourseSerializer