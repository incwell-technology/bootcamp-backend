from visitor import models as visitor_models
from rest_framework import viewsets, permissions
from .serializers import StudentSerializer, TalkSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = visitor_models.Student.objects.order_by("-id").all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentSerializer


class TalkViewSet(viewsets.ModelViewSet):
    queryset = visitor_models.Talk_To_Mentor.objects.order_by("-id").all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TalkSerializer

