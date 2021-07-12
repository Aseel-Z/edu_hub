from rest_framework import serializers
from .models import Member, Message, Post, Connection

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id','local','city','member', 'first_name', 'last_name', 'organization_name', 'gender', 'birth_date', 'password', 'email', 'mobile_number', 'specialization', 'interests', 'biography', 'current_organization', 'organization_summary', 'freelancer', 'hourly_tutoring_rate', 'services', 'created_at', 'updated_at')

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