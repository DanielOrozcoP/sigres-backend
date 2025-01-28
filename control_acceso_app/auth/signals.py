from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    try:
        # Intentar crear los grupos
        # Grupo Administrador
        admin_group, _ = Group.objects.get_or_create(name='Administrador')
        
        # Grupo Especialista
        especialista_group, _ = Group.objects.get_or_create(name='Especialista')
        
        # Grupo Estudiante
        estudiante_group, _ = Group.objects.get_or_create(name='Estudiante')

        # Asignar permisos si existen
        try:
            # Aquí van tus asignaciones de permisos actuales
            # Si algún permiso no existe, se saltará esa asignación
            pass
        except Permission.DoesNotExist:
            # Los permisos específicos no existen aún
            pass

    except Exception as e:
        # Log del error pero permitir que la aplicación continúe
        print(f"Error al crear grupos: {str(e)}")
        pass



