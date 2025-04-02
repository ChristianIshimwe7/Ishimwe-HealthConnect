from django.shortcuts import render

def home(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def service(request):
    return render(request, 'core/service.html')

def contact(request):
    return render(request, 'core/contact.html')

def login(request):
    return render(request, 'core/login.html')

def admin_dashboard(request):
    return render(request, 'core/admin_dashboard.html')



from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.conf import settings
from twilio.rest import Client  # Import Twilio API for SMS functionality

from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user registration
            # Redirect to the success page
            return redirect('success_page')  
        else:
            # Handle validation errors and render the form again
            return render(request, 'core/signup.html', {'form': form, 'error': "User registration with this Email already exists."})
    else:
        form = UserRegistrationForm()
    return render(request, 'core/signup.html', {'form': form})



def success_page(request):
    return render(request, 'core/success.html', {'message': 'Congratulations on signing up! Please log in to continue.'})




