from django.apps import AppConfig


# make sure to update AppClassName and App name
# AppBoilerplateSmallConfig
class GeneralConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = 'apps.general'
    verbose_name = 'app general of django project'
    label = 'general'
