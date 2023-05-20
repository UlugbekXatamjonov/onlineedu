from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryAPIViewset, SubCategoryAPIViewset, ExampAPIViewset, QuestionAPIViewset, \
    AnswerAPIViewset, ResultAPIViewset

router = DefaultRouter()
router.register(r'category', CategoryAPIViewset, 'category')
router.register(r'subcategory', SubCategoryAPIViewset, 'subcategory')
router.register(r'examp', ExampAPIViewset, 'examp')
router.register(r'question', QuestionAPIViewset, 'question')
router.register(r'answer', AnswerAPIViewset, 'answer')
router.register(r'result', ResultAPIViewset, 'result')

urlpatterns = [ 
    path('', include(router.urls))
]




