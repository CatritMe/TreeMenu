import os

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

User = get_user_model()

ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', default='admin')
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', default='admin@admin.com')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', default='admin')


class Command(BaseCommand):
    _class = User
    name = 'SUPERUSER'

    def handle(self, *args, **kwargs):
        self._class.objects.create_superuser(
            ADMIN_USERNAME, ADMIN_EMAIL, ADMIN_PASSWORD)
