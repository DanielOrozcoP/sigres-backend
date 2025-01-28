from django.test import TestCase, Client
from django.urls import reverse
from proceso_app.models.cuarto import Cuarto
from proceso_app.models.dormitorio import Dormitorio
from proceso_app.models.edificio import Edificio
from proceso_app.models.sede import Sede
from proceso_app.models.estudiante import Estudiante
from django.db.models import F
from rest_framework import status
import json

class CuartoServicesTests(TestCase):
    def setUp(self):
        """Configuración inicial para los tests"""
        self.client = Client()
        
        # Crear datos de prueba
        self.sede = Sede.objects.create(
            codigo="SP001",
            nombre="Sede de Prueba",
            direccion="Dirección de prueba"
        )
        
        self.edificio = Edificio.objects.create(
            codigo="EP001",
            sexo=True,  # True para masculino, por ejemplo
            sedeID=self.sede
        )
        
        self.dormitorio = Dormitorio.objects.create(
            codigo="DP001",
            descricpion="Dormitorio de prueba",
            edificioID=self.edificio
        )
        
        # Crear varios cuartos con diferentes estados
        self.cuarto_vacio = Cuarto.objects.create(
            codigo="C101",
            capacidad=4,
            ocupacion=0,
            dormitorioID=self.dormitorio
        )
        
        self.cuarto_medio_lleno = Cuarto.objects.create(
            codigo="C102",
            capacidad=4,
            ocupacion=2,
            dormitorioID=self.dormitorio
        )
        
        self.cuarto_lleno = Cuarto.objects.create(
            codigo="C103",
            capacidad=4,
            ocupacion=4,
            dormitorioID=self.dormitorio
        )
        
        # Crear estudiante de prueba
        self.estudiante = Estudiante.objects.create(
            carnet_identidad="12345678901",
            nombre="Estudiante",
            apellido="Prueba",
            facultad="Facultad de Prueba",
            carrera="Carrera de Prueba",
            ano_academico=2,
            cuarto=self.cuarto_medio_lleno
        )

    def test_get_cuarto_free_sin_parametros(self):
        """Test para obtener cuartos libres sin parámetros"""
        url = reverse('cuarto-free')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        
        # Debería devolver 2 cuartos (vacío y medio lleno)
        self.assertEqual(data['metadata']['total_cuartos'], 2)
        self.assertTrue(any(c['codigo'] == "C101" for c in data['cuartos_disponibles']))
        self.assertTrue(any(c['codigo'] == "C102" for c in data['cuartos_disponibles']))

    def test_get_cuarto_free_con_filtros(self):
        """Test para obtener cuartos libres con filtros"""
        url = reverse('cuarto-free')
        params = {
            'sede_id': self.sede.codigo,
            'capacidad_min': 3,
            'ordenar_por': 'disponibilidad'
        }
        response = self.client.get(url, params)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        
        # Verificar que los filtros se aplicaron correctamente
        self.assertTrue(all(c['capacidad'] >= 3 for c in data['cuartos_disponibles']))

    def test_get_cuarto_free_sin_resultados(self):
        """Test para verificar respuesta cuando no hay cuartos disponibles"""
        # Llenar todos los cuartos
        Cuarto.objects.all().update(ocupacion=F('capacidad'))
        
        url = reverse('cuarto-free')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertEqual(data['metadata']['total_cuartos'], 0)
        self.assertEqual(len(data['cuartos_disponibles']), 0)

    def test_asignar_cuarto_exitoso(self):
        """Test para asignar cuarto exitosamente"""
        url = reverse('asignar-cuarto')
        params = {
            'estudiante_id': self.estudiante.carnet_identidad,
            'sede_id': self.sede.codigo
        }
        response = self.client.get(url, params)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertIn('cuarto_sugerido', data)
        self.assertIn('mensaje', data)

    def test_asignar_cuarto_estudiante_no_existe(self):
        """Test para verificar error cuando el estudiante no existe"""
        url = reverse('asignar-cuarto')
        params = {
            'estudiante_id': '99999999999',
            'sede_id': self.sede.codigo
        }
        response = self.client.get(url, params)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        data = json.loads(response.content)
        self.assertIn('error', data)

    def test_asignar_cuarto_sin_estudiante_id(self):
        """Test para verificar error cuando no se proporciona estudiante_id"""
        url = reverse('asignar-cuarto')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = json.loads(response.content)
        self.assertIn('error', data) 