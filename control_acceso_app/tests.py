from django.test import TestCase
from django.contrib.auth.models import Group, Permission
from control_acceso_app.auth.signals import create_groups

class AuthenticationTests(TestCase):
    def setUp(self):
        """Configurar grupos y permisos para pruebas"""
        create_groups(None)  # Crear grupos manualmente para las pruebas
    
    def test_grupos_creados(self):
        """Verificar que los grupos se crean correctamente"""
        grupos_esperados = ['Administrador', 'Especialista', 'Estudiante']
        for grupo in grupos_esperados:
            self.assertTrue(Group.objects.filter(name=grupo).exists())
    
    # Más tests relacionados con autenticación... 
