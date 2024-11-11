from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from proceso_app.models import sede, edificio,estudiante,dormitorio,cuarto
from django.contrib.auth.models import User


def create_admin_group():
    #? Grupo de Permisos para el admin
    admin_group, created = Group.objects.get_or_create(name='admin')
    content_type = ContentType.objects.get_for_model(User)
    permissions_codename = ['add_user','change_user','delete_user','view_user']
    for codename in permissions_codename:
        permiso = Permission.objects.get(codename=codename, content_type=content_type)
        admin_group.permissions.add(permiso)

def create_directivo_group():
    directivo_group, created = Group.objects.get_or_create(name='directivo')
    content_types = ContentType.objects.get_for_models(sede.Sede, edificio.Edificio, dormitorio.Dormitorio, cuarto.Cuarto, estudiante.Estudiante)
    permissions_codename = ['view_sede','view_edificio','view_dormitorio','view_cuarto',"view_estudiante"]
    # Obtener todos los permisos una vez
    all_permissions = Permission.objects.filter(codename__in=permissions_codename, content_type__in=content_types.values())
    # Crear un diccionario para acceso rápido a permisos
    permission_dict = {perm.codename: perm for perm in all_permissions}
    # Asignar permisos al grupo
    for codename in permissions_codename:
        permiso = permission_dict.get(codename)
        if permiso:
            directivo_group.permissions.add(permiso)

def create_j_beca_group():
    j_beca_group, created = Group.objects.get_or_create(name='j_beca')
    content_type = ContentType.objects.get_for_model(estudiante.Estudiante)
    permissions_codename = ['add_estudiante','change_estudiante','delete_estudiante','view_estudiante']
    for codename in permissions_codename:
        permiso = Permission.objects.get(codename=codename, content_type=content_type)
        j_beca_group.permissions.add(permiso)

def create_especialista_groups():
    # Crear el grupo especialista
    especialista_group, created = Group.objects.get_or_create(name='especialista')
    # Obtener ContentTypes para los modelos relevantes
    content_types = ContentType.objects.get_for_models(sede.Sede, edificio.Edificio, dormitorio.Dormitorio, cuarto.Cuarto, estudiante.Estudiante)
    permissions_codename = ['add', 'change', 'delete', 'view']
    # Asignar permisos al grupo especialista para cada modelo
    for model_name, ct in content_types.items():
        for codename in permissions_codename:
            permission_codename = f"{codename}_{str(model_name).split('.')[2]}"
            permiso = Permission.objects.get(codename=permission_codename, content_type=ct)
            especialista_group.permissions.add(permiso)
