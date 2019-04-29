from rest_framework import serializers
from visitor import models as visitor_models


class EnrollSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = "__all__"
        model = visitor_models.Enroll


class TalkSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = "__all__"
        model = visitor_models.Talk_To_Mentor
