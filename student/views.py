from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from django.forms.models import model_to_dict
from pprint import pprint

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken


from .models import Student
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, \
    UserChangePasswordSerializer, SendPasswordResetEmailSerializer, \
    UserPasswordResetSerializer, LogoutSerializer
from .renderers import UserRenderer



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'token': token, 'message': "Ro'yhatdan muvaffaqiyatli o'tdingiz"}, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            token = get_tokens_for_user(user)
            active_user = Student.objects.get(id=user.id)
            serializer = UserProfileSerializer(active_user)
            return Response({
                'token': token,
                'user_profile_data': serializer.data,
                'message': 'Tizimga muvaffaqiyatli kirdingiz',
            }, status=status.HTTP_200_OK)

        else:
            return Response({
                'errors': {
                    'non_field_errors': ["Kiritilgan 'parol' yoki 'username' noto'g'ri"]
                }
            }, status=status.HTTP_404_NOT_FOUND)


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    permission_classes = (IsAuthenticated,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UserProfileView(RetrieveUpdateDestroyAPIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserProfileUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = UserProfileSerializer()
    lookup_field = 'slug'

    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        student_data = self.get_object()
        data = request.data

        try:
            if Student.objects.filter(username=data['username']) and student_data.username != data['username']:
                return Response({'error': "Bunday 'username' avval yaratilgan ! Iltimos boshqa 'username' tanlang."}, status=status.HTTP_204_NO_CONTENT)
        except: 
            pass

        try:
            student_data.password = data['password'] if 'password' in data else student_data.password
            student_data.username = data['username'] if 'username' in data else student_data.username
            student_data.first_name = data['first_name'] if 'first_name' in data else student_data.first_name
            student_data.last_name = data['last_name'] if 'last_name' in data else student_data.last_name
            student_data.age = data['age'] if 'age' in data else student_data.age
            student_data.gender = data['gender'] if 'gender' in data else student_data.gender
            student_data.ball = data['ball'] if 'ball' in data else student_data.ball
            student_data.coin = data['coin'] if 'coin' in data else student_data.coin
            student_data.email = data['email'] if 'email' in data else student_data.email
            student_data.phone = data['phone'] if 'phone' in data else student_data.phone

            student_data.save()
            serializer = UserProfileSerializer(student_data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'errors': "Ma'lumotlarni saqlashda xatolik sodir bo'ladi!!!"}, status=status.HTTP_204_NO_CONTENT)


class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(
            data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'message': "Parol muvaffaqiyatli o'zgartirildi"}, status=status.HTTP_200_OK)


class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'message': "Parolni tiklash uchun link yuborildi. Iltimos emailingizni tekshiring"}, status=status.HTTP_200_OK)


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(
            data=request.data, context={'uid': uid, 'token': token})
        serializer.is_valid(raise_exception=True)
        return Response({'message': 'Parol muvaffaqiyatli yangilandi'}, status=status.HTTP_200_OK)


"""  ------------------------------------------------  """
