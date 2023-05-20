from django.shortcuts import render
from pprint import pprint

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from exam.models import Category, SubCategory, Examp, Question, Answer, Result
from .serializers import CategoryAPISerializer, SubCategoryAPISerializer, ExampAPISerializer, \
    QuestionAPISerializer, AnswerAPISerializer, ResultAPISerializer


# Create your views here.

class CategoryAPIViewset(ModelViewSet):
    queryset =  Category.objects.filter(status=True)
    serializer_class = CategoryAPISerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SubCategoryAPIViewset(ModelViewSet):
    queryset =  SubCategory.objects.filter(status=True)
    serializer_class = SubCategoryAPISerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ExampAPIViewset(ModelViewSet):
    queryset =  Examp.objects.filter(status=True)
    serializer_class = ExampAPISerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class QuestionAPIViewset(ModelViewSet):
    queryset =  Question.objects.filter(status=True)
    serializer_class = QuestionAPISerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class AnswerAPIViewset(ModelViewSet):
    queryset =  Answer.objects.filter(status=True)
    serializer_class = AnswerAPISerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ResultAPIViewset(ModelViewSet):
    queryset =  Result.objects.filter(status=True)
    serializer_class = ResultAPISerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
