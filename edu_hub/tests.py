from django.urls import reverse
from rest_framework.test import APITestCase
from edu_hub.models import Message, Connection, Post

class PostTests(APITestCase):

    def test_home_page_status_code(self):
        url = reverse('member_list')
        response = self.client.get(url) 
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_status_code(self):
        url = reverse('member_detail', args = [1,])
        response = self.client.get(url)
        # It gives 401 because the authentication. 
        self.assertEqual(response.status_code, 404)


    def test_show_connections(self):
        url = reverse("show_connections")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_show_connections_primary(self):
        url = reverse('show_connections_primary', args = [1,])
        response = self.client.get(url)
        # It gives 401 because the authentication. 
        self.assertEqual(response.status_code, 404)

        
    def test_show_message(self):
        url = reverse('show_message')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_show_message_primary(self):
        url = reverse('show_message_primary', args = [1,])
        response = self.client.get(url)
        # It gives 401 because the authentication. 
        self.assertEqual(response.status_code, 404)


    def test_show_post(self):
        url = reverse('show_post')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_show_post_primary(self):
        url = reverse('show_post_primary', args = [1,])
        response = self.client.get(url)
        # It gives 401 because the authentication. 
        self.assertEqual(response.status_code, 404)