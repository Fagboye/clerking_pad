from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import User_Profile

class AccountsViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('user_registration')
        self.login_url = reverse('user_login')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword123',
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        }
    # Test user registration
    def test_user_registration(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    # Test user login
    def test_user_login(self):
        # First, create a user
        User.objects.create_user(username='testuser', password='testpassword123')

        login_data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    # Test invalid login
    def test_invalid_login(self):
        login_data = {
            'username': 'nonexistentuser',
            'password': 'wrongpassword'
        }
        response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # Test token refresh
    def test_token_refresh(self):
        # First, create a user and get tokens
        User.objects.create_user(username='testuser', password='testpassword123')
        login_response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpassword123'
        }, format='json')
        refresh_token = login_response.data['refresh']

        # Now try to refresh the token
        refresh_url = reverse('token_refresh')
        response = self.client.post(refresh_url, {'refresh': refresh_token}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
