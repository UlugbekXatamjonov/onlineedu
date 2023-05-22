from django.contrib import admin
from .models import Category, SubCategory, Examp, Question, Answer, Result, FreeResult

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','id', 'status', 'created_at')
    list_filter = ('status','created_at')
    list_editable = ('status',)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','id', 'category', 'status', 'created_at')
    list_filter = ('category', 'status','created_at')
    list_editable = ('status',)

@admin.register(Examp)
class ExampAdmin(admin.ModelAdmin):
    list_display = ('name','id', 'lesson', 'main_examp', 'time', 'status', 'created_at')
    list_filter = ('lesson', 'main_examp','status','created_at')
    list_editable = ('status',)

class AnswerTabularAdmin(admin.TabularInline):
    model = Answer
    fields = ('answer_text', 'question', 'true_answer', 'status')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'id', 'subcategory', 'examp', 'status', 'created_at')
    list_filter = ('subcategory','examp','status','created_at')
    list_editable = ('status',)
    inlines = [AnswerTabularAdmin,]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_text','id','question', 'true_answer', 'status', 'created_at')
    list_filter = ('question','true_answer', 'status', 'created_at')
    list_editable  = ('true_answer','status')
    
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'subcategory', 'examp', 'ball', 'coin', 'status', 'created_at')
    list_filter = ('subcategory', 'examp', 'status', 'created_at')

@admin.register(FreeResult)
class FreeResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'subcategory', 'ball', 'created_at')

