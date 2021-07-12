from rest_framework import generics
from users.models import Message, Post, Connection
from edu_hub.serializers import MessageSerializer, PostSerializer, ConnectionSerializer


class ConnectionList(generics.ListCreateAPIView):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer

class ConnectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer

    

class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
