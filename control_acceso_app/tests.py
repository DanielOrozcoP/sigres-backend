from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from control_acceso_app.auth.serializers import RegistrationSerializer

class AuthTests(APITestCase):

    def setUp(self):
        # Crear un usuario para las pruebas
        self.username = 'testuser'
        self.password = 'testpassword'
        self.password2 = 'testpassword'
        self.email = 'testemail@gmail.com'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_success(self):
        """Prueba de inicio de sesión exitoso"""
        url = reverse('login')  # Asegúrate de que el nombre de la URL sea correcto
        response = self.client.post(url, {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_invalid_credentials(self):
        """Prueba de inicio de sesión con credenciales incorrectas"""
        url = reverse('login')
        response = self.client.post(url, {'username': self.username, 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Credenciales incorrectas')

    def test_registration_success(self):
        """Prueba de registro exitoso"""
        url = reverse('register')  # Asegúrate de que el nombre de la URL sea correcto
        data = {
            'username': 'newuser',
            'password': 'newpassword',
            'email': 'newuser@example.com'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
        self.assertEqual(response.data['username'], 'newuser')

    def test_registration_existing_user(self):
        """Prueba de registro de un usuario existente"""
        url = reverse('register')
        data = {
            'username': self.username,
            'password': self.password,
            'email': 'existinguser@example.com'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)

    def test_registration_invalid_data(self):
        """Prueba de registro con datos inválidos"""
        url = reverse('register')
        data = {
            'username': '',  # Nombre de usuario vacío
            'password': 'short',  # Contraseña demasiado corta
            'email': 'not-an-email'  # Correo electrónico no válido
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)
        self.assertIn('password', response.data)
        self.assertIn('email', response.data)

    def test_login_without_credentials(self):
        """Prueba de inicio de sesión sin credenciales"""
        url = reverse('login')
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_without_credentials(self):
        """Prueba de registro sin credenciales"""
        url = reverse('register')
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
