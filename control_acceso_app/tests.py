from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import status
from rest_framework.test import APIClient
from proceso_app.models.cuarto import Cuarto  # Para asignar permisos

class AuthenticationTests(TestCase):
    def setUp(self):
        """Configuración inicial para las pruebas"""
        self.client = APIClient()
        
        # Crear grupos usando get_or_create
        self.admin_group, _ = Group.objects.get_or_create(name='admin')
        self.directivo_group, _ = Group.objects.get_or_create(name='directivo')
        self.j_beca_group, _ = Group.objects.get_or_create(name='j_beca')
        self.especialista_group, _ = Group.objects.get_or_create(name='especialista')
        
        # Asignar permisos al grupo especialista
        content_type = ContentType.objects.get_for_model(Cuarto)
        permisos = Permission.objects.filter(content_type=content_type)
        for permiso in permisos:
            self.especialista_group.permissions.add(permiso)
        
        # Crear usuario de prueba
        self.test_user = User.objects.create_user(
            username='test_user',
            email='test@example.com',
            password='test_password123'
        )
        
        # Asignar al grupo especialista
        self.test_user.groups.add(self.especialista_group)

    def test_registro_exitoso(self):
        """Test para registro de usuario exitoso"""
        url = reverse('register')
        data = {
            'username': 'nuevo_usuario',
            'email': 'nuevo@example.com',
            'password': 'password123',
            'password2': 'password123',
            'group': 'estudiante'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='nuevo_usuario').exists())
        self.assertIn('token', response.data)
        self.assertIn('roles', response.data)

    def test_registro_passwords_no_coinciden(self):
        """Test para verificar validación de passwords que no coinciden"""
        url = reverse('register')
        data = {
            'username': 'nuevo_usuario',
            'email': 'nuevo@example.com',
            'password': 'password123',
            'password2': 'password456',
            'group': 'estudiante'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registro_email_duplicado(self):
        """Test para verificar validación de email duplicado"""
        url = reverse('register')
        data = {
            'username': 'otro_usuario',
            'email': 'test@example.com',  # Email que ya existe
            'password': 'password123',
            'password2': 'password123',
            'group': 'estudiante'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_obtener_token(self):
        """Test para obtener token JWT"""
        url = reverse('token_obtain_pair')
        data = {
            'username': 'test_user',
            'password': 'test_password123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_token_credenciales_invalidas(self):
        """Test para verificar rechazo de credenciales inválidas"""
        url = reverse('token_obtain_pair')
        data = {
            'username': 'test_user',
            'password': 'wrong_password'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_grupos_creados(self):
        """Test para verificar la creación correcta de grupos"""
        grupos_esperados = ['admin', 'directivo', 'j_beca', 'especialista']
        for grupo in grupos_esperados:
            self.assertTrue(Group.objects.filter(name=grupo).exists())

    def test_permisos_especialista(self):
        """Test para verificar los permisos del grupo especialista"""
        grupo = Group.objects.get(name='especialista')
        permisos = grupo.permissions.all()
        self.assertTrue(permisos.exists())
        # Aquí puedes agregar verificaciones específicas de permisos

    def test_refresh_token(self):
        """Test para verificar el refresh del token"""
        # Primero obtener los tokens
        url = reverse('token_obtain_pair')
        data = {
            'username': 'test_user',
            'password': 'test_password123'
        }
        response = self.client.post(url, data, format='json')
        refresh_token = response.data['refresh']

        # Intentar refrescar el token
        url = reverse('token_refresh')
        data = {'refresh': refresh_token}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    # Más tests relacionados con autenticación... 
