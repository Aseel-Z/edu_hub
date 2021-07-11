from rest_framework import generics
from edu_hub.models import Member, Message, Chat, Post, Connection


class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()



class ConnectionList(generics.ListCreateAPIView):
    queryset = Connection.objects.all()

class ConnectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Connection.objects.all()



class ChatList(generics.ListCreateAPIView):
    queryset = Chat.objects.all()

class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()



class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()