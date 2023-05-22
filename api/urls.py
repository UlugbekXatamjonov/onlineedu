from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryAPIViewset, SubCategoryAPIViewset, ExampAPIViewset, QuestionAPIViewset, \
    AnswerAPIViewset, ResultAPIViewset, TeacherViewset, CourseViewset, FreeResultAPIViewset, MyCourseViewSet

router = DefaultRouter()
""" --------------------------- EXAM APP --------------------------- """
router.register(r'examp/category', CategoryAPIViewset, 'category')
router.register(r'examp/subcategory', SubCategoryAPIViewset, 'subcategory')
router.register(r'examp/examp', ExampAPIViewset, 'examp')
router.register(r'examp/question', QuestionAPIViewset, 'question')
router.register(r'examp/answer', AnswerAPIViewset, 'answer')
router.register(r'examp/result', ResultAPIViewset, 'result')
router.register(r'examp/free-result', FreeResultAPIViewset, 'free-result')

""" --------------------------- COURSE APP --------------------------- """
router.register(r'course/course', CourseViewset, 'course')
router.register(r'course/teacher', TeacherViewset, 'teacher')
router.register(r'course/mycourse', MyCourseViewSet, 'mycourse')


urlpatterns = [ 
    path('', include(router.urls))
]




