"""from django.urls import path
from . import views

urlpatterns = [
    # Example endpoint: Replace or add more as needed.
    path('patients/', views.PatientListCreateAPIView.as_view(), name='patient-list-create'),
    # If you have another view for retrieve, update, destroy
    path('patients/<int:pk>/', views.PatientRetrieveUpdateDestroyAPIView.as_view(), name='patient-detail'),
]"""


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('signup/', views.signup, name='signup'),
    path('success/', views.success_page, name='success_page'),
]
