from rest_framework import serializers
from edu_hub.models import Message, Post, Connection

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("__all__")

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')

class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ('__all__')