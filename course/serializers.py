from rest_framework.serializers import ModelSerializer

from .models import Course, Lessons, Teacher, File, MyCourse


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ('__all__')

class LessonsSerializer(ModelSerializer):
    class Meta:
        model = Lessons
        fields = ('__all__')

class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('__all__')

class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = ('__all__')

class MyCourseSerializer(ModelSerializer):
  class Meta:
     model = MyCourse
     fields = ('__all__')



