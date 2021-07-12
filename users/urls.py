from django.urls import path

from .views import MemberList, MemberDetail #, ConnectionList, ConnectionDetail, MessageList, MessageDetail, PostList, PostDetail

urlpatterns = [
    path("show_members/", MemberList.as_view(), name = 'member_list'),
    path("show_members/<int:pk>/", MemberDetail.as_view(), name = 'member_detail'),
    # path("show_connections/", ConnectionList.as_view()),
    # path("show_connections/<int:pk>/", ConnectionDetail.as_view()),
    # path("show_message/", MessageList.as_view()),
    # path("show_message/<int:pk>/", MessageDetail.as_view()),
    # path("show_post/", PostList.as_view()),
    # path("show_post/<int:pk>/", PostDetail.as_view()),
]