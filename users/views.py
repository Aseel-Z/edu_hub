from rest_framework import generics
from users.models import User
from users.serializers import UserDetailsSerializer, LoginSerializer, UserSignUp #SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class MemberList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer


class LoginView(generics.RetrieveAPIView):
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    error_messages = {
        'invalid': "Invalid username or password",
        'disabled': "Sorry, this account is suspended",
    }

    def _error_response(self, message_key):
        data = {
            'success': False,
            'message': self.error_messages[message_key],
            'user_id': None,
        }

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        city = request.POST.get('city')
        member = request.POST.get('member')
        mobile_number = request.POST.get('mobile_number')
        specialization = request.POST.get('specialization')
        interests = request.POST.get('interests')
        biography = request.POST.get('biography')
        hourly_tutoring_rate = request.POST.get('hourly_tutoring_rate')
        gender = request.POST.get('gender')
        organization_summary = request.POST.get('organization_summary')
        user = authenticate(email=email, password=password, first_name=first_name, city=city, member=member, mobile_number=mobile_number, specialization=specialization, interests=interests, biography=biography, hourly_tutoring_rate=hourly_tutoring_rate, gender=gender, organization_summary=organization_summary)
        # user = authenticate(email=email, password=password)        
        if user is not None:
            if user.is_active:
                login(request, user)

                return Response(status=status.HTTP_100_OK)
            return self._error_response('disabled')
        return self._error_response('invalid')


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUp

# Add Logout 