from django.urls import path
from django.contrib.auth import views as auth_views

from .views import MemberList, MemberDetail, SignUpView

urlpatterns = [
    path("login/show_members/", MemberList.as_view(), name = 'member_list'),
    path("show_members/<int:pk>/", MemberDetail.as_view(), name = 'member_detail'),
    path("signup/", SignUpView.as_view(), name= "user_sign_up")
]