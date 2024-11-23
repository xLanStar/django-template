import os

import django
import environ

environ.Env.read_env()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

django.setup()
