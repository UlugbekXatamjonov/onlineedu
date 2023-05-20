from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Teacher, Course, Lessons, File
from .serializers import CourseSerializer, LessonsSerializer, TeacherSerializer, FileSerializer

# Create your views here.

class TeacherViewset(ModelViewSet):
    queryset  = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny]

class CourseViewset(ModelViewSet):
    queryset  = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

class LessonViewset(ModelViewSet):
    queryset  = Lessons.objects.all()
    serializer_class = LessonsSerializer
    permission_classes = [AllowAny]

class FileViewset(ModelViewSet):
    queryset  =File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [AllowAny]



