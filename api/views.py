from django.shortcuts import render
from pprint import pprint
import json

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from student.models import Student
from course.models import Course, Teacher, Lessons, File, MyCourse
from exam.models import Category, SubCategory, Examp, Question, Answer, Result, \
    FreeResult, FreeCategory, FreeSubCategory
from course.serializers import MyCourseSerializer
from .serializers import CategoryAPISerializer, SubCategoryAPISerializer, ExampAPISerializer, \
    QuestionAPISerializer, AnswerAPISerializer, ResultAPISerializer, CourseAPISerializer,\
    TeacherAPISerializer, MyCourseAPISerializer, FreeResultAPISerializer, FileAPISerializer, \
    LessonAPISerializer, FreeSubCategoryAPISerializer, FreeCategoryAPISerializer


# Create your views here.
""" --------------------------- EXAM APP --------------------------- """

class CategoryAPIViewset(ModelViewSet):
    queryset =  Category.objects.filter(status=True)
    serializer_class = CategoryAPISerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

class SubCategoryAPIViewset(ModelViewSet):
    queryset =  SubCategory.objects.filter(status=True)
    serializer_class = SubCategoryAPISerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

class ExampAPIViewset(ModelViewSet):
    queryset =  Examp.objects.filter(status=True)
    serializer_class = ExampAPISerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

class QuestionAPIViewset(ModelViewSet):
    queryset =  Question.objects.filter(status=True)
    serializer_class = QuestionAPISerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

class AnswerAPIViewset(ModelViewSet):
    queryset =  Answer.objects.filter(status=True)
    serializer_class = AnswerAPISerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

class ResultAPIViewset(ModelViewSet):
    queryset =  Result.objects.all()
    serializer_class = ResultAPISerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    def create(self, request, *args, **kwargs):
        request_data = request.data

        """ Obyekt ko'rinishidagi malumotlarni aniqlashtisrib olamiz """
        try:
            if 'examp' in request_data:
                examp = Examp.objects.get(id=int(request_data['examp']))
            else:
                examp = None

            if 'subcategory' in request_data:
                subcategory = SubCategory.objects.get(id=int(request_data['subcategory']))
            else:
                subcategory = None

            student = Student.objects.get(id=int(request_data['student']))
        except Exception as e:
            return Response({'error':"Ma'lumotlar kiritilishida xatolik bo'lgan !!!"})
        
        result_ball = 0
        result_coin = 0
        keys = json.loads(request_data['answers'])
        for key in keys:
            answer = Answer.objects.get(id=key)
            if answer.true_answer == True:
                result_ball += 1
                result_coin += 1

                student.ball += 1
                student.coin += 1
                student.save()

        try:
            new_result = Result.objects.create(
                student = student,
                subcategory = subcategory,
                examp = examp,
                ball = result_ball,
                coin = result_coin,
                status = True,
            )
            new_result.save()
            serializer = ResultAPISerializer(new_result)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error':"Ma'lumotlarni saqlashda xatolik yuzaga keldi !!!"})


class FreeCategoryAPIViewset(ModelViewSet):
    queryset =  FreeCategory.objects.filter(status=True)
    serializer_class = FreeCategoryAPISerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

class FreeSubCategoryAPIViewset(ModelViewSet):
    queryset =  FreeSubCategory.objects.filter(status=True)
    serializer_class = FreeSubCategoryAPISerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

class FreeResultAPIViewset(ModelViewSet):
    queryset =  FreeResult.objects.all()
    serializer_class = FreeResultAPISerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

    def create(self, request, *args, **kwargs):
        request_data = request.data

        """ Obyekt ko'rinishidagi malumotlarni aniqlashtisrib olamiz """
        try:
            if 'subcategory' in request_data:
                subcategory = FreeSubCategory.objects.get(id=int(request_data['subcategory']))
            else:
                subcategory = None
        except Exception as e:
            return Response({'error':"Ma'lumotlar kiritilishida xatolik bo'lgan !!!"})
        
        result_ball = 0
        keys = json.loads(request_data['answers'])
        for key in keys:
            answer = Answer.objects.get(id=key)
            if answer.true_answer == True:
                result_ball += 1

        try:
            new_result = FreeResult.objects.create(
                subcategory = subcategory,
                ball = result_ball,
            )
            new_result.save()
            serializer = FreeResultAPISerializer(new_result)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error':"Ma'lumotlarni saqlashda xatolik yuzaga keldi !!!"})


""" --------------------------- COURSE APP --------------------------- """
class FileViewset(ModelViewSet):
    queryset  = File.objects.filter(status=True)
    serializer_class = FileAPISerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

class LessonViewset(ModelViewSet):
    queryset  = Lessons.objects.filter(status=True)
    serializer_class = LessonAPISerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

class TeacherViewset(ModelViewSet):
    queryset  = Teacher.objects.filter(status=True)
    serializer_class = TeacherAPISerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

class CourseViewset(ModelViewSet):
    queryset  = Course.objects.filter(status=True)
    serializer_class = CourseAPISerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

class MyCourseViewSet(ModelViewSet):
    queryset = MyCourse.objects.filter(status=True)
    serializer_class = MyCourseAPISerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    
    def create(self, request, *args, **kwargs):
        request_data = request.data

        try:
            student = Student.objects.get(id=request.user.id)
        except Exception as e:
            return Response({'error':"Bunday o'quvchi topilmadi"})

        try:
            if 'course' in request_data:
                course = Course.objects.get(id=request_data['course'])
            else:
                return Response({'error':"Bunday kurs topilmadi"})
        except Exception as e:
            return Response({'error':"Kursning ma'lumotlarini saqlashda xatolik yuzaga keldi"})

        print(course)
        print(type(course))
        for key, value in course.items():
            print(key, value)

        new_my_course = MyCourse.objects.create(
            student = student,
            course = course,
            next_lesson = None,
        )
        new_my_course.save()
        serializer = MyCourseAPISerializer(new_my_course)
        return Response(serializer.data)



