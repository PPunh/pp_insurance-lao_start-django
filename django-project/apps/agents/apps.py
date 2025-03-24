from django.apps import AppConfig


# make sure to update AppClassName and App name
class AppBoilerplateSmallConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = 'apps.agents'
    verbose_name = 'Insurance Agents'
    label = 'agents'
