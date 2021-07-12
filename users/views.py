from rest_framework import generics
from users.models import User
from users.serializers import UserDetailsSerializer, RegisterSerializer


class MemberList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer

    
