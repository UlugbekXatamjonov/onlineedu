from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, \
    SendPasswordResetEmailView, UserPasswordResetView, LogoutAPIView,  UserProfileUpdateView, \
    MyCourseViewset, ContactViewset

router = DefaultRouter()
router.register(r'mycourse', MyCourseViewset, 'mycourse')
router.register(r'contact', ContactViewset, 'contact')

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="registration"),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('profile/update/<slug:slug>/', UserProfileUpdateView.as_view(), name="profile_update"),
    path('profile/', UserProfileView.as_view(), name="profile"),
    path('change-password/', UserChangePasswordView.as_view(), name="change_password"),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name="send_reset_password_email"),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),

    path('', include(router.urls))
]







