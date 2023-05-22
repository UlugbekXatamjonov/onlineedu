from django.urls import path, include
from rest_framework import routers

from .views import TeacherViewset, CourseViewset, LessonViewset, FileViewset,MyCourseViewset

router = routers.DefaultRouter()
router.register(r'teacher', TeacherViewset, 'teacher')
router.register(r'course', CourseViewset, 'course')
router.register(r'lesson', LessonViewset, 'lesson')
router.register(r'file', FileViewset, 'file')
router.register(r'mycourse', MyCourseViewset, 'mycourse')


urlpatterns = [
    path('', include(router.urls))
]



