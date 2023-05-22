from rest_framework import serializers
from exam.models import Category, SubCategory, Examp, Question, Answer, Result, FreeResult
from course.models import Course, Teacher, Lessons, File, MyCourse

        
""" --------------------------- EXAM APP --------------------------- """
class FreeResultAPISerializer(serializers.ModelSerializer):
    class Meta: 
        model = FreeResult
        fields = ('id', 'subcategory','ball', 'slug')

class ResultAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'student','subcategory','examp', 'slug', 'ball','coin')

class AnswerAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'question', 'answer_text', 'slug')

class QuestionAPISerializer(serializers.ModelSerializer):
    answers = AnswerAPISerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ('id', 'subcategory', 'examp', 'question_text', 'slug', 'answers')

class ExampAPISerializer(serializers.ModelSerializer):
    questions = QuestionAPISerializer(many=True, read_only=True)
    class Meta:
        model = Examp
        fields = ('id', 'name', 'slug', 'lesson', 'main_examp', 'about', 'time', 'questions')

class SubCategoryAPISerializer(serializers.ModelSerializer):
    questions = QuestionAPISerializer(many=True, read_only=True)
    class Meta:
        model = SubCategory
        fields = ('id', 'category','name', 'slug', 'questions')

class CategoryAPISerializer(serializers.ModelSerializer):
    subcategories = SubCategoryAPISerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'subcategories')


""" --------------------------- COURSE APP --------------------------- """

class TeacherAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'full_name', 'slug', 'age', 'degree', 'about', 'status')

class CourseAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'slug', 'teacher', 'lesson_count', 'cost', 'status')

class MyCourseAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCourse
        fields = ('id', 'student', 'slug', 'course', 'coin', 'ball')







