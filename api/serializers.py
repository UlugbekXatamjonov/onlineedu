from rest_framework import serializers
from exam.models import Category, SubCategory, Examp, Question, Answer, Result

        
class ResultAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'student','subcategory','examp','ball','coin')

class AnswerAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'question', 'answer_text')

class QuestionAPISerializer(serializers.ModelSerializer):
    answers = AnswerAPISerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ('id', 'subcategory', 'examp', 'question_text', 'answers')

class ExampAPISerializer(serializers.ModelSerializer):
    questions = QuestionAPISerializer(many=True, read_only=True)
    class Meta:
        model = Examp
        fields = ('id', 'name', 'lesson', 'main_examp', 'about', 'time', 'questions')

class SubCategoryAPISerializer(serializers.ModelSerializer):
    questions = QuestionAPISerializer(many=True, read_only=True)
    class Meta:
        model = SubCategory
        fields = ('id', 'category','name', 'questions')

class CategoryAPISerializer(serializers.ModelSerializer):
    subcategories = SubCategoryAPISerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'name','subcategories')


