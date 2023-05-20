from rest_framework import serializers

from .models import Category, SubCategory, Examp, Question, Answer, Result

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('__all__')

class ExampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examp
        fields = ('__all__')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('__all__')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('__all__')

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'ball', 'coin', 'subcategory')



