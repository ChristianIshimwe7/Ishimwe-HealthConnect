"""from django.contrib import admin
from django.urls import path, include  # Import include for linking app-level URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('api/', include('core.urls')),  # Connect to URLs from the 'core' app
]




from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Define a simple home view for the root URL.
def home(request):
    return HttpResponse("Welcome to Ishimwe HealthConnect!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # Routes for your API endpoints.
    path('', home, name='home'),  # This route handles the root URL ("/")
]"""



"""from django.contrib import admin
from django.urls import path, include
from core.views import home, about, service, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('contact/', contact, name='contact'),
]"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),              # Admin interface
    path('api/', include('core.urls')),           # APIs and other routes under '/api/'
    path('', include('core.urls')),               # Core routes for home, about, etc.
]

