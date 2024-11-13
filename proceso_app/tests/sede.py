from django.test import TestCase
from proceso_app.models.sede import Sede
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User

class SedeTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.especialista_user = User.objects.create_user(username='especialista', password='12345')
        self.user_without_permission = User.objects.create_user(username='normal_user', password='12345')

    def test_sede_create_view_valid_data(self):
        url = reverse('sede-create')
        data = {
            'nombre': 'Sede Test',
            'direccion': 'Calle Test 123',
            'telefono': '1234567890'
        }
        self.client.force_authenticate(user=self.especialista_user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sede.objects.count(), 1)
        self.assertEqual(Sede.objects.get().nombre, 'Sede Test')

    def test_sede_create_invalid_data(self):
        url = reverse('sede-create')
        invalid_data = {
            'nombre': '',  # Empty name, which should be invalid
            'direccion': 'Test Address',
        }
        self.client.force_authenticate(user=self.especialista_user)
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('nombre', response.data)

    # ... (rest of the test methods)

    def test_sede_create_view_unauthorized(self):
        url = reverse('sede-create')
        data = {'nombre': 'Test Sede', 'direccion': 'Test Address'}
        self.client.force_authenticate(user=self.user_without_permission)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)