from rest_framework import serializers
from exam.models import Category, SubCategory, Examp, Question, Answer, Result, \
    FreeResult, FreeCategory, FreeSubCategory
from course.models import Course, Teacher, Lessons, File, MyCourse, Unit

        
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

class FreeSubCategoryAPISerializer(serializers.ModelSerializer):
    questions = QuestionAPISerializer(many=True, read_only=True)
    class Meta:
        model = FreeSubCategory
        fields = ('id', 'category','name', 'slug', 'questions')

class FreeCategoryAPISerializer(serializers.ModelSerializer):
    free_subcategories = FreeSubCategoryAPISerializer(many=True, read_only=True)
    class Meta:
        model = FreeCategory
        fields = ('id', 'name', 'slug', 'free_subcategories')


""" --------------------------- COURSE APP --------------------------- """

class TeacherAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'full_name', 'slug', 'age', 'degree', 'about', 'status')

class FileAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file',)

class LessonAPISerializer(serializers.ModelSerializer):
    files = FileAPISerializer(many=True, read_only=True)
    examp = ExampAPISerializer(many=True, read_only=True)
    class Meta:
        model = Lessons
        fields = ('id', 'name', 'slug', 'unit', 'about', 'video', 'body', 'files', 'examp')

class UnitAPISerializer(serializers.ModelSerializer):
    lessons = LessonAPISerializer(many=True, read_only=True)
    class Meta:
        model = Unit
        fields = ('id', 'name', 'slug', 'course', 'lessons')

class CourseAPISerializer(serializers.ModelSerializer):
    units = UnitAPISerializer(many=True, read_only=True)
    teacher_name = serializers.CharField(source='teacher.full_name')
    class Meta:
        model = Course
        fields = ('id', 'name', 'slug', 'teacher', 'teacher_name', 'lesson_count', 'cost', 'about', 'photo',\
                  'units'
                  )

class MyCourseAPISerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.name')
    course_lesson_count = serializers.IntegerField(source='course.lesson_count')
    course_slug = serializers.CharField(source='course.slug')
    
    class Meta:
        model = MyCourse
        fields = ('id', 'student', 'slug', 'course', 'course_name', 'course_slug', 'course_lesson_count',\
                   'coin', 'ball', 'next_lesson')






