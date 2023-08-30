from django.db.migrations import serializer
from django.shortcuts import render, get_object_or_404
from rest_framework import status, generics
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from mysite.resttest.models import Course, Klass, Subject, Mentor, Student
from mysite.resttest.serializers import CourseSerializer, ClassSerializer, SubjectSerializer, MentorSerializer, \
    StudentSerializer


class CoursesViews(ListAPIView):
    permission_classes = (IsAuthenticated, )
    pagination_class = PageNumberPagination
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        items = Course.objects.all
        serializer = CourseSerializer(items, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

class ClassesViews(APIView):
    permission_classes = (IsAuthenticated, )
    def post(self, request):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        items = Klass.objects.all()
        serializer = ClassSerializer
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


class CourseViews(APIView):
    def get(self, request, id):
        item = get_object_or_404(Course, id=id)
        serializer = CourseSerializer(item)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id):
        item = get_object_or_404(Course, id=id)
        serializer = CourseSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        item = get_object_or_404(Course, id=id)
        item.delete()
        return Response({"data": None}, status=status.HTTP_200_OK)

class ClassViews():
    def get(self, request, id):
        item = get_object_or_404(Klass, id=id)
        serializer = ClassSerializer(item)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id):
        item = get_object_or_404(Klass, id=id)
        serializer = ClassSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        item = get_object_or_404(Klass, id=id)
        item.delete()
        return Response({"data": None}, status=status.HTTP_200_OK)


class SubjectViews(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class MentorViews(generics.ListCreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer


class StudentViews(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class MentorCourseListViews(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = CourseSerializer

