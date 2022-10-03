from django.apps import AppConfig


class GestExportConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GestExport'
    verbose_name = 'GestExport'  # Permite cambiar el nombre del Proyecto asociandolo tambien en el archivo Settings en INSTALLED_APPS = 'gestExport.apps.GestForestConfig',
