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

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Twilio SMS Sending
            account_sid = settings.TWILIO_ACCOUNT_SID
            auth_token = settings.TWILIO_AUTH_TOKEN
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"Welcome {user.full_name}! Your registration is successful.",
                from_=settings.TWILIO_PHONE_NUMBER,
                to=user.phone_number
            )
            return redirect('success_page')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/signup.html', {'form': form})


def success_page(request):
    return render(request, 'success.html', {'message': "Registration successful!"})

from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.conf import settings
from twilio.rest import Client  # Twilio library for sending SMS





