from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Member, Message, Chat, Connection, Post
# Create your tests here.

# class MemberModelTests(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         test_user_member = get_user_model().objects.create(username='admin',password='admin')
#         test_user_member.save()

#         test_member = Member.objects.create(
#             local = True ,
#             city = "Amman", 
#             member = test_user_member,
#             first_name = 'Yahya' ,
#             last_name = 'Omari', 
#             organization_name = "LTUC",
#             gender = "M",
#             birth_date = "1998-07-01T09:32:25Z",
#             password = "admin",
#             email = "yahya@example.com",
#             mobile_number = "0777777777",
#             specialization = "test",
#             interests = "Coding and football",
#             biography = "Software developer",
#             current_organization = "LTUC",
#             organization_summary = "Teach",
#             freelancer = False,
#             hourly_tutoring_rate = 1,
#             services = "Teaching ",
#             created_at = "2021-07-11T09:31:41Z",
#             updated_at = "2021-07-11T09:31:43Z",
#         )
#         test_member.save()

#     def test_blog_content(self):
#         post = Member.objects.get(id=1)

#         self.assertEqual(post.local, "educator")
#         self.assertEqual(post.city, 'Amman')
#         self.assertEqual(str(post.member), 'admin')
#         self.assertEqual(post.first_name, 'Yahya')
#         self.assertEqual(post.last_name, 'Omari')
#         self.assertEqual(post.organization_name, 'LTUC')
#         self.assertEqual(post.gender, 'M')
#         self.assertEqual(post.birth_date, '1998-07-01T09:32:25Z')
#         self.assertEqual(post.password, 'admin')
#         self.assertEqual(post.email, 'yahya@example.com')
#         self.assertEqual(post.mobile_number, '0777777777')
#         self.assertEqual(post.specialization, 'test')
#         self.assertEqual(post.interests, 'Coding and football')
#         self.assertEqual(post.biography, 'Software developer')
#         self.assertEqual(post.current_organization, 'LTUC')
#         self.assertEqual(post.organization_summary, 'Teach')
#         self.assertEqual(post.freelancer, False)
#         self.assertEqual(post.hourly_tutoring_rate, 1)
#         self.assertEqual(post.services, 'Teaching')
#         self.assertEqual(post.created_at, "2021-07-11T09:31:41Z")
#         self.assertEqual(post.updated_at, "2021-07-11T09:31:43Z")

class PostTests(APITestCase):

    def test_home_page_status_code(self):
        url = reverse('show_members')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_status_code(self):
        url = reverse('show_members_primary')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        

    def test_home_page_status_code(self):
        url = reverse('show_connections')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_status_code(self):
        url = reverse('show_connections_primary')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        

    def test_home_page_status_code(self):
        url = reverse('show_chat')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_status_code(self):
        url = reverse('show_chat_primary')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        

    def test_home_page_status_code(self):
        url = reverse('show_message')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_status_code(self):
        url = reverse('show_message_primary')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        

    def test_home_page_status_code(self):
        url = reverse('show_post')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_status_code(self):
        url = reverse('show_post_primary')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)