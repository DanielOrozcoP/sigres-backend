from django.db.models.signals import post_migrate
from django.dispatch import receiver
from control_acceso_app.auth.groups import create_directivo_group,create_especialista_groups,create_admin_group,create_j_beca_group

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    create_directivo_group(),create_especialista_groups(),create_admin_group(),create_j_beca_group()



