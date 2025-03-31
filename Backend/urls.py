"""from django.urls import path
from . import views

urlpatterns = [
    # Example endpoint: Replace or add more as needed.
    path('patients/', views.PatientListCreateAPIView.as_view(), name='patient-list-create'),
    # If you have another view for retrieve, update, destroy
    path('patients/<int:pk>/', views.PatientRetrieveUpdateDestroyAPIView.as_view(), name='patient-detail'),
]"""


from django.contrib import admin
from django.urls import path, include
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Include the `core` app's URLs
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Include routes from the core app
]
