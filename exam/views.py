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
    permission_classes = [IsAuthenticated]

class SubCategoryViewset(ModelViewSet):
    queryset =  SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsAuthenticated]

class ExampViewset(ModelViewSet):
    queryset =  Examp.objects.all()
    serializer_class = ExampSerializer
    permission_classes = [IsAuthenticated]

class QuestionViewset(ModelViewSet):
    queryset =  Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

class AnswerViewset(ModelViewSet):
    queryset =  Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

class ResultViewset(ModelViewSet):
    queryset =  Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]

