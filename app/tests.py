from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class AuthenticationTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('registration_register')
        self.login_url = reverse('auth_login')

    def test_register(self):
        response = self.client.post(self.register_url, {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_login(self):
        user = User.objects.create_user(username='testuser', password='testpassword123')

        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpassword123'
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        user = User.objects.get(username='testuser')
        self.assertTrue(user.is_authenticated)


