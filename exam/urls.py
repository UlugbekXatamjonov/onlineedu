from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewset, SubCategoryViewset, ExampViewset, QuestionViewset, \
    AnswerViewset, ResultViewset

router = DefaultRouter()
# router.register(r'category', CategoryViewset, 'category')
# router.register(r'subcategory', SubCategoryViewset, 'subcategory')
# router.register(r'exam', ExampViewset, 'exam')
# router.register(r'question', QuestionViewset, 'question')
# router.register(r'answer', AnswerViewset, 'answer')
router.register(r'result', ResultViewset, 'result')

urlpatterns = [
    path('', include(router.urls))
]




