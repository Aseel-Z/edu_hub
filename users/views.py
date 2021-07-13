from rest_framework import generics
from users.models import User
from users.serializers import UserDetailsSerializer, LoginSerializer, SignUpForm
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


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(request, email=user.email, password=raw_password)
#             if user is not None:
#                 login(request, user)
#             else:
#                 print("user is not authenticated")
#             return redirect('users:profile')
#     else:
#         form = SignUpForm()
#     return render(request, '../templates/signup.html', {'form': form})


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
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return Response(status=status.HTTP_100_OK)
            return self._error_response('disabled')
        return self._error_response('invalid')


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = '../templates/signup.html'
    success_url = reverse_lazy('login')
    form_class = SignUpForm
    success_message = "Your profile was created successfully"
