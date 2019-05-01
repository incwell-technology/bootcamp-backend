from rest_framework import serializers
from visitor import models as visitor_models
from syllabus import models as syllabus_models


class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = "__all__"
        model = visitor_models.Student

    def create(self, validated_data):
        student = visitor_models.Student(
            firstName=validated_data['firstName'],
            middleName=validated_data['middleName'],
            lastName=validated_data['lastName'],
            email=validated_data['email'],
            gender=validated_data['gender'],
            education=validated_data['education'],
            phone=validated_data['phone'],
            gitLink=validated_data['gitLink']
        )
        student.save()
        for data in validated_data['course']:
            student.course.add(data)
            
        # visitor_models.Enroll.objects.create(student=student, course=validated_data['course'])    
        return student

class TalkSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = "__all__"
        model = visitor_models.Talk_To_Mentor
