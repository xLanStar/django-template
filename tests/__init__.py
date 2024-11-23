import os
from pathlib import Path

import django
import environ

env_path = Path(__name__).parent / ".env"
environ.Env.read_env(env_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

django.setup()
