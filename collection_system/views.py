
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .forms import CompanyForm, CustomerRequestForm, LoginForm, RegistrationForm
from .models import  CustomerRequest,Company
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import CustomerRequestForm
from .models import CustomerRequest



def make_request(request):
    if request.method == 'POST':
        form = CustomerRequestForm(request.POST)
        if form.is_valid():
            request_obj = form.save(commit=False)
            if request.user.is_authenticated:
                request_obj.user = request.user
            else:
                messages.error(request, 'Please log in to make a request.')
                return redirect('home')
            request_obj.save()
            return redirect('payment', request_id=request_obj.pk)
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        request_id = request.GET.get('request_id')
        if request_id:
            request_instance = get_object_or_404(CustomerRequest, pk=request_id)
            form = CustomerRequestForm(instance=request_instance)
        else:
            form = CustomerRequestForm()
    
    return render(request, 'make_request.html', {'form': form})


def payment(request, request_id):
    # Fetch the request object based on request_id
    request_obj = CustomerRequest.objects.get(pk=request_id)

    # Placeholder for payment processing logic
    if request.method == 'POST':
        # Add your payment processing logic here
        # For example:
        # if payment_is_successful:
        #     messages.success(request, 'Payment successful!')
        # else:
        #     messages.error(request, 'Payment failed. Please try again.')
        #     return redirect('payment', request_id=request_id)
        messages.success(request, 'Payment successful!')
        return redirect('home')  # Redirect to home page after successful payment

    return render(request, 'payment.html', {'request_obj': request_obj})



def company_detail(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    return render(request, 'company_detail.html', {'company': company})


@login_required
def home(request):
    companies = Company.objects.all()
    return render(request, 'home.html', {'companies': companies})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in!')
                return redirect('home')  # Redirect to home page after successful login
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


from django.shortcuts import redirect

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'You have successfully registered!')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')
