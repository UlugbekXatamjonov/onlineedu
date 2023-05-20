from django.urls import path, include
from rest_framework import routers

from .views import TeacherViewset, CourseViewset, LessonViewset, FileViewset

router = routers.DefaultRouter()
router.register(r'teacher', TeacherViewset, 'teacher')
router.register(r'course', CourseViewset, 'course')
router.register(r'lesson', LessonViewset, 'lesson')
router.register(r'file', FileViewset, 'file')


urlpatterns = [
    path('', include(router.urls))
]



