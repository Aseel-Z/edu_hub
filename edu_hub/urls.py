from django.urls import path

from .views import MemberList, MemberDetail, ConnectionList, ConnectionDetail, ChatList, ChatDetail, MessageList, MessageDetail, PostList, PostDetail

urlpatterns = [
    path("/show_members/", MemberList.as_view()),
    path("/show_members/<int:pk>/", MemberDetail.as_view()),
    path("/show_connections/", ConnectionList.as_view()),
    path("/show_connections/<int:pk>/", ConnectionDetail.as_view()),
    path("/show_chat/", ChatList.as_view()),
    path("/show_chat/<int:pk>/", ChatDetail.as_view()),
    path("/show_message/", MessageList.as_view()),
    path("/show_message/<int:pk>/", MessageDetail.as_view()),
    path("/show_post/", PostList.as_view()),
    path("/show_post/<int:pk>/", PostDetail.as_view()),
]