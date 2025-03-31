import os
from django.core.asgi import get_asgi_application

# Set the default settings module for the 'Ishimwe_HealthConnect' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ishimwe_HealthConnect.settings')

application = get_asgi_application()
