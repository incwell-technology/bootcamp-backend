from bootcamp import models as bootcamp_models
from rest_framework import viewsets, permissions
from .serializers import CompanySerializer, MentorSerializer, ContentSerializer, SkillSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = bootcamp_models.Company.objects.order_by("-id").all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CompanySerializer


class MentorViewSet(viewsets.ModelViewSet):
    queryset = bootcamp_models.Mentor.objects.order_by("-id").all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MentorSerializer


class ContentViewSet(viewsets.ModelViewSet):
    queryset = bootcamp_models.Content.objects.order_by("-id").all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ContentSerializer


