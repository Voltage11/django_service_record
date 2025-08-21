from django.apps import AppConfig


class ServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.service'
    verbose_name = 'Сервисные записи'
    verbose_name_plural = 'Сервисные записи'
