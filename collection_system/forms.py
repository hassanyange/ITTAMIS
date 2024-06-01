

from django import forms
from .models import Company, CustomerRequest, UserProfile, User, Ward, District, Street
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'location']


class CustomerRequestForm(forms.ModelForm):
    phone_number = forms.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', 'Enter a 10-digit phone number.')],
        required=True
    )
    email = forms.EmailField(required=True)
    national_id_number = forms.CharField(max_length=20, required=True)
    amount_to_invest = forms.DecimalField(max_digits=10, decimal_places=2, required=True)

    class Meta:
        model = CustomerRequest
        fields = ['full_name', 'phone_number', 'email', 'national_id_number', 'amount_to_invest']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        if len(phone_number) != 10:
            raise forms.ValidationError("Phone number must be exactly 10 digits.")
        return phone_number

    def clean_national_id_number(self):
        national_id_number = self.cleaned_data.get('national_id_number')
        if not national_id_number.isdigit():
            raise forms.ValidationError("National ID number must contain only digits.")
        return national_id_number

    def clean_amount_to_invest(self):
        amount_to_invest = self.cleaned_data.get('amount_to_invest')
        if amount_to_invest <= 0:
            raise forms.ValidationError("Amount to invest must be a positive number.")
        return amount_to_invest

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        return email


        
from django.contrib.auth.password_validation import validate_password

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    location = forms.CharField(max_length=255)
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        validators=[validate_password]  # Ensure strong password
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput,
        validators=[validate_password]  # Ensure strong password
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'location']

    def clean_password2(self):
        # Check if passwords match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['location'] 
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']