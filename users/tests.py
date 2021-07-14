from django.test import TestCase
from django.contrib.auth import get_user_model


class UserAccountTests(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'testuser@super.com', 'username', 'firstname', 'password')
        self.assertEqual(super_user.email, 'testuser@super.com')
        self.assertEqual(super_user.user_name, 'username')
        self.assertEqual(super_user.first_name, 'firstname')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), "username")

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com', user_name='username1', first_name='first_name', password='password', is_superuser=False)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com', user_name='username1', first_name='first_name', password='password', is_staff=False)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='', user_name='username1', first_name='first_name', password='password', is_superuser=True)

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            'testuser@user.com', 'username', 'firstname', 'password')
        self.assertEqual(user.email, 'testuser@user.com')
        self.assertEqual(user.user_name, 'username')
        self.assertEqual(user.first_name, 'firstname')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)

        with self.assertRaises(ValueError):
            db.objects.create_user(
                email='', user_name='a', first_name='first_name', password='password')










# /////////////////////////////////////
# /////////////////////////////////////
# /////////////////////////////////////

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
import datetime

from rest_framework import status
from rest_framework.test import APITestCase

from .models import User
# Create your tests here.

class PostTests(APITestCase):


    def test_home_page_status_code(self):
        url = reverse('member_list')
        response = self.client.get(url)
        # It gives 401 because the authentication. 
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_status_code(self):
        url = reverse('member_detail', args = [1,])
        response = self.client.get(url)
        # It gives 401 because the authentication. 
        self.assertEqual(response.status_code, 404)


    def test_show_connections(self):
        url = reverse('user_sign_up')
        response = self.client.get(url)
        # It gives 401 because the authentication. 
        self.assertEqual(response.status_code, 405)
    



#     def test_show_connections_primary(self):
#         url = reverse('show_connections_primary', args = [1,])
#         response = self.client.get(url)
#         # It gives 401 because the authentication. 
#         self.assertEqual(response.status_code, 401)

        

#     def test_show_message(self):
#         url = reverse('show_message')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 401)
    
#     def test_show_message_primary(self):
#         url = reverse('show_message_primary', args = [1,])
#         response = self.client.get(url)
#         # It gives 401 because the authentication. 
#         self.assertEqual(response.status_code, 401)

        

#     def test_show_post(self):
#         url = reverse('show_post')
#         response = self.client.get(url)
#         # It gives 401 because the authentication. 
#         self.assertEqual(response.status_code, 401)
    
#     def test_show_post_primary(self):
#         url = reverse('show_post_primary', args = [1,])
#         response = self.client.get(url)
#         # It gives 401 because the authentication. 
#         self.assertEqual(response.status_code, 401)

class MemberModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user_member = get_user_model().objects.create(username='admin',password='admin')
        test_user_member.save()

        test_member = User.objects.create(
            username = "admin",
            email = "yahya@example.com",
            first_name = 'Yahya' ,
            last_name = 'Omari', 
            is_active = True, 
            is_staff = True ,
            is_superuser = True ,
            created_at = "2020-07-12",
            birth_date = "1998-07-01",
            local = True ,
            city = "Amman", 
            member = 'educator',
            organization_name = "LTUC",
            gender = "M",
            # password = "admin",
            mobile_number = int("0777777777"),
            specialization = "test",
            interests = "Coding and football",
            biography = "Software developer",
            current_organization = "LTUC",
            organization_summary = "Teach",
            website = "https://www.google.com",
            freelancer = False,
            hourly_tutoring_rate = 1,
            services = "Teaching ",
            updated_at = "2021-07-12",
        )
        test_member.save()

    def test_blog_content(self):
        post = User.objects.get(id=1)

        self.assertEqual(post.username, 'admin')
        self.assertEqual(post.email, 'yahya@example.com')
        self.assertEqual(post.first_name, 'Yahya')
        self.assertEqual(post.last_name, 'Omari')
        self.assertEqual(post.is_active, True)
        self.assertEqual(post.is_staff, True)
        self.assertEqual(post.is_superuser, True)
        self.assertEqual(post.created_at, datetime.date(2020, 7, 12))
        self.assertEqual(post.birth_date, datetime.date(1998, 7, 1))
        self.assertEqual(post.local, True)
        self.assertEqual(post.city, 'Amman')
        self.assertEqual(post.member, "educator")
        self.assertEqual(post.organization_name, 'LTUC')
        self.assertEqual(post.gender, 'M')
        # self.assertEqual(post.password, 'admin')
        self.assertEqual(post.mobile_number, 777777777)
        self.assertEqual(post.specialization, 'test')
        self.assertEqual(post.interests, 'Coding and football')
        self.assertEqual(post.biography, 'Software developer')
        self.assertEqual(post.current_organization, 'LTUC')
        self.assertEqual(post.organization_summary, 'Teach')
        self.assertEqual(post.website, 'https://www.google.com')
        self.assertEqual(post.freelancer, False)
        self.assertEqual(post.hourly_tutoring_rate, 1)
        self.assertEqual(post.services, 'Teaching ')
        self.assertEqual(post.updated_at, datetime.date(2021, 7, 12))