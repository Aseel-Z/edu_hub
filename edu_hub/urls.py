from django.urls import path


from .views import ConnectionList, ConnectionDetail, MessageList, MessageDetail, PostList, PostDetail

urlpatterns = [
    path("show_connections/", ConnectionList.as_view(), name = 'show_connections'),
    path("show_connections/<int:pk>/", ConnectionDetail.as_view(), name = 'show_connections_primary'),
    path("show_message/", MessageList.as_view(), name = 'show_message'),
    path("show_message/<int:pk>/", MessageDetail.as_view(), name = 'show_message_primary'),
    path("show_post/", PostList.as_view(), name = 'show_post'),
    path("show_post/<int:pk>/", PostDetail.as_view(), name = 'show_post_primary'),
   
]