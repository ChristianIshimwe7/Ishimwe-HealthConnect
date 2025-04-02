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

def success_page(request):
    return render(request, 'core/success.html', {'message': 'Signup successful! Please log in.'})



from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.conf import settings
from twilio.rest import Client

from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

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


from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, PatientForm
from .models import UserRegistration, Patient
from django.contrib.auth.hashers import check_password
from django.conf import settings
from twilio.rest import Client

def home(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def service(request):
    return render(request, 'core/service.html')

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Saves to database with hashed password
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            message = client.messages.create(
                body=f"Welcome to Ishimwe HealthConnect, {user.full_name}! Signup successful.",
                from_=settings.TWILIO_PHONE_NUMBER,
                to=user.phone_number
            )
            return redirect('success_page')
        else:
            return render(request, 'core/signup.html', {'form': form, 'error': "Email already exists or invalid data."})
    else:
        form = UserRegistrationForm()
    return render(request, 'core/signup.html', {'form': form})

def success_page(request):
    return render(request, 'core/success.html', {'message': 'Signup successful! Please log in.'})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = UserRegistration.objects.get(email=email)
            if check_password(password, user.password):
                request.session['user_id'] = user.id  # Store user ID in session
                return redirect('treatment')  # Redirect to treatment page
            else:
                return render(request, 'core/login.html', {'error': 'Invalid credentials'})
        except UserRegistration.DoesNotExist:
            return render(request, 'core/login.html', {'error': 'User not found'})
    return render(request, 'core/login.html')

def admin_dashboard(request):
    return render(request, 'core/admin_dashboard.html')

def treatment(request):
    if 'user_id' not in request.session:
        return redirect('login')  # Ensure user is logged in

    user = UserRegistration.objects.get(id=request.session['user_id'])
    patients = Patient.objects.filter(user=user)  # Get patient's data for this user

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            new_patient = form.save(commit=False)
            new_patient.user = user
            # Suggest medicine based on existing patients
            patient_category = new_patient.categorize_age()
            for patient in patients:
                if (patient.categorize_age() == patient_category and
                    patient.service == new_patient.service and
                    patient.hospital == new_patient.hospital and
                    patient.medicine):
                    new_patient.medicine = patient.medicine
                    break
            new_patient.save()  # Save to database
            return render(request, 'core/treatment.html', {
                'form': PatientForm(),
                'patients': patients,
                'message': f"Patient {new_patient.name} recorded. Suggested medicine: {new_patient.medicine or 'None'}"
            })
    else:
        form = PatientForm()

    return render(request, 'core/treatment.html', {'form': form, 'patients': patients})









# core/views.py (partial update for treatment function)
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, PatientForm
from .models import UserRegistration, Patient
from django.contrib.auth.hashers import check_password
from django.conf import settings
from twilio.rest import Client

# ... (other views remain unchanged)

def treatment(request):
    if 'user_id' not in request.session:
        return redirect('login')
    user = UserRegistration.objects.get(id=request.session['user_id'])
    patients = Patient.objects.filter(user=user)
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            new_patient = form.save(commit=False)
            new_patient.user = user
            new_patient.save()
            return render(request, 'core/treatment.html', {
                'form': PatientForm(),
                'patients': patients,
                'message': f"Patient {new_patient.name} recorded."
            })
    else:
        form = PatientForm()
    return render(request, 'core/treatment.html', {'form': form, 'patients': patients})