from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Mentor, Student, Klass, Course, Subject


class MentorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mentor
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)

    class Meta:
        model = Student


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("__all__")


class MentorCourseSerializer(serializers.ModelSerializer):


    class Meta:
        model = Course
        fields = ("__all__")


class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Klass
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
