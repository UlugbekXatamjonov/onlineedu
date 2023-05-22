from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Teacher, Course, Lessons, File, MyCourse
from .serializers import CourseSerializer, LessonsSerializer, TeacherSerializer, FileSerializer, MyCourseSerializer

# Create your views here.

class TeacherViewset(ModelViewSet):
    queryset  = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CourseViewset(ModelViewSet):
    queryset  = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class LessonViewset(ModelViewSet):
    queryset  = Lessons.objects.all()
    serializer_class = LessonsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class FileViewset(ModelViewSet):
    queryset  =File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MyCourseViewset(ModelViewSet):
    queryset = MyCourse.objects.all()
    serializer_class = MyCourseSerializer
    permission_classes = [AllowAny]


