from rest_framework import serializers
from users.models import Message, Post, Connection

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id','create_date','message_body','creator_id')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','create_date','post_body','creator_id')

class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ('id','connection_member_id','member_id','connection_date')