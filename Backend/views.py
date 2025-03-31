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
            user = form.save()  # Save the user's data in the database
            
            # Send SMS
            account_sid = 'your_account_sid'  # Replace with your Twilio Account SID
            auth_token = 'your_auth_token'  # Replace with your Twilio Auth Token
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"Welcome {user.full_name}! Your registration is successful.",
                from_='+1234567890',  # Replace with your Twilio phone number
                to=user.phone_number  # User's phone number
            )
            
            return redirect('success_page')  # Redirect to a success page
    else:
        form = UserRegistrationForm()

    return render(request, 'signup.html', {'form': form})



def success_page(request):
    return render(request, 'success.html', {'message': "Registration successful!"})








