from django.test import TestCase

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

class APIScenarioAuthenticationTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct_signin_url(self):
        """Session based authentication page is exist.

            check: Status code assertion
        """
        response = self.client.get('/api/v1/signin/')
        self.assertEqual(response.status_code, 200)

    def test_correct_jwt_token_url(self):
        """JWT authentication token generation is exist on api server

            check: Status code assertion
        """
        response = self.client.get('/api/v1/jwt/token/')
        self.assertEqual(response.status_code, 200)

    def test_correct_jwt_token_url(self):
        """JWT authentication refresh is exist on api server

            check: Status code assertion
        """
        response = self.client.get('/api/v1/jwt/token/refresh')
        self.assertEqual(response.status_code, 200)

    def test_correct_jwt_token_auth(self):
        """Json Web Token use for JavaScript frameworks like react.
        
            check: Status code assertion
            check: token generation
            check: refresh token
        """
        
        response = self.client.post('/api/v1/auth-token/', {'username':'test', 'password':'12test12'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('refresh' in response.data)
        self.assertIn('access' in response.data)
        response = self.client.post('/api/v1/auth-token/refresh', {'refresh':response.data['refresh']})
        self.assertEqual(response.status_code, 200)
        self.assertIn('access' in response.data)

    def test_correct_token_url(self):
        """Token based authentication page is exist.

            check: status code assertion
        """
        response = self.client.get('/api/v1/auth-token/')
        self.assertEqual(response.status_code, 200)

    def test_correct_token_auth(self):
        """Token authentication use devices like android, ios.
            
            check: status code assertion
            check: token is generated
            check: email is exist
        """
        response = self.client.post('/api/v1/auth-token/', {'username':'test', 'password':'12test12'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('token' in response.data)
        self.assertIn('email' in response.data)


    

