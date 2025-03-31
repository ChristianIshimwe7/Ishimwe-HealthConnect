import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'Ishimwe_HealthConnect' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ishimwe_HealthConnect.settings')

application = get_wsgi_application()
