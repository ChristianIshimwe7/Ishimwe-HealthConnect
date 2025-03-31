"""
URL configuration for Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
from django.urls import path, include  # Import include to incorporate URLs from your apps

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('api/', include('core.urls')),  # API endpoints from your core app
]"""

"""from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simple home view that returns a welcome message.
def home(request):
    return HttpResponse("Welcome to Ishimwe HealthConnect!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # Route to your API endpoints
    path('', home, name='home'),          # This pattern handles the root URL "/"
]"""

from django.urls import path
from core.views import home, about, service, contact, login, admin_dashboard


from core import views


urlpatterns = [
    path('', home, name='home'),                 # Displays index.html
    path('about/', about, name='about'),         # Displays about.html
    path('service/', service, name='service'),   # Displays service.html
    path('contact/', contact, name='contact'),   # Displays contact.html
    path('login/', login, name='login'),         # Displays login.html
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'), # Displays admin_dashboard.html
    path('signup/', views.signup, name='signup'),
    path('success/', views.success_page, name='success_page'),  # Add a success page

    
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # This links to the core app's URLs
]



