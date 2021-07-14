from .models import User
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

class UserAccountTests(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'username', 'testuser@super.com', 'password')
        self.assertEqual(super_user.email, 'testuser@super.com')
        self.assertEqual(super_user.username, 'username')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), "username")

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            'username', 'testuser@user.com', 'password')
        self.assertEqual(user.email, 'testuser@user.com')
        self.assertEqual(user.username, 'username')
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_active)


class PostTests(APITestCase):
    def test_home_page_status_code(self):
        url = reverse('member_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_about_page_status_code(self):
        url = reverse('member_detail', args = [1, ])
        response = self.client.get(url)
        # It gives 401 because the authentication.
        self.assertEqual(response.status_code, 404)

    def test_show_connections(self):
        url = reverse('user_sign_up')
        response = self.client.get(url)
        # It gives 401 because the authentication.
        self.assertEqual(response.status_code, 405)



class MemberModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_member = User.objects.create(
        username= "admin13",
        email= "yahya@example.com",
        first_name = 'Yahya',
        last_name = 'Omari',
        is_active = True,
        is_staff = True,
        is_superuser = True,
        created_at= "2020-07-12",
        local = True,
        city = "Amman",
        member= 'educator',
        organization_name= "LTUC",
        gender= "M",
        mobile_number= int("0777777777"),
        specialization= "test",
        interests= "Coding and football",
        biography= "Software developer",
        current_organization= "LTUC",
        organization_summary= "Teach",
        website= "https://www.google.com",
        freelancer= False,
        hourly_tutoring_rate= 1,
        services= "Teaching ",
        )
        test_member.save()


    def test_blog_content(self):
        post = User.objects.get(id=1)
        self.assertEqual(post.username, 'admin13')
        self.assertEqual(post.email,'yahya@example.com')
        self.assertEqual(post.first_name, 'Yahya')
        self.assertEqual(post.last_name, 'Omari')
        self.assertEqual(post.is_active, True)
        self.assertEqual(post.is_staff, True)
        self.assertEqual(post.is_superuser, True)
        self.assertEqual(post.local, True)
        self.assertEqual(post.city, 'Amman')
        self.assertEqual(post.member, "educator")
        self.assertEqual(post.organization_name, 'LTUC')
        self.assertEqual(post.gender, 'M')
        self.assertEqual(post.mobile_number, '777777777')
        self.assertEqual(post.specialization, 'test')
        self.assertEqual(post.interests, 'Coding and football')
        self.assertEqual(post.biography, 'Software developer')
        self.assertEqual(post.current_organization, 'LTUC')
        self.assertEqual(post.organization_summary, 'Teach')
        self.assertEqual(post.website, 'https://www.google.com')
        self.assertEqual(post.freelancer, False)
        self.assertEqual(post.hourly_tutoring_rate, 1)
        self.assertEqual(post.services, 'Teaching ')
