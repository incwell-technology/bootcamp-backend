from visitor import models as visitor_models
from rest_framework import viewsets, permissions
from .serializers import EnrollSerializer, TalkSerializer


class EnrollViewSet(viewsets.ModelViewSet):
    queryset = visitor_models.Enroll.objects.order_by("-id").all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EnrollSerializer


class TalkViewSet(viewsets.ModelViewSet):
    queryset = visitor_models.Talk_To_Mentor.objects.order_by("-id").all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TalkSerializer