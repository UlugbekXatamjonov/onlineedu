from django.shortcuts import render
from pprint import pprint
import json

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Category, SubCategory, Examp, Question, Answer, Result
from .serializers import SubCategorySerializer, ExampSerializer, QuestionSerializer,\
      AnswerSerializer, CategorySerializer, ResultSerializer
from student.models import Student

# Create your views here.

class CategoryViewset(ModelViewSet):
    queryset =  Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class SubCategoryViewset(ModelViewSet):
    queryset =  SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [AllowAny]

class ExampViewset(ModelViewSet):
    queryset =  Examp.objects.all()
    serializer_class = ExampSerializer
    permission_classes = [AllowAny]

class QuestionViewset(ModelViewSet):
    queryset =  Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]

class AnswerViewset(ModelViewSet):
    queryset =  Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [AllowAny]

class ResultViewset(ModelViewSet):
    queryset =  Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [AllowAny]

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
            serializer = ResultSerializer(new_result)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error':"Ma'lumotlarni saqlashda xatolik yuzaga keldi !!!"})


