from django.apps import AppConfig


class ControlAccesoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'control_acceso_app'

    def ready(self):
        import control_acceso_app.auth.signals