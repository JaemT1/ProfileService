# perfiles/apps.py
from threading import Thread
import subprocess

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

    def ready(self):
        import rabbitmq_consumer
        def start_rabbitmq_consumer():
            subprocess.call(['python', 'manage.py', 'start_rabbitmq_consumer'])

        Thread(target=start_rabbitmq_consumer, daemon=True).start()
