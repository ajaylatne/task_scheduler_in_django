from django.apps import AppConfig
from . import updater
import os


class App1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1'

    def ready(self):
        if os.environ.get('RUN_MAIN'):
            updater.start()
