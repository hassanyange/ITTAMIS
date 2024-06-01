from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone

class CompanyProfile(models.Model):
    company_name = models.CharField(max_length=50)
    company_description = models.TextField()
    picture = models.ImageField (upload_to='static/images')

    def __str__(self):
        return self.company_name

    


class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=255, blank=True)
    types_of_garbage = models.TextField(max_length=255, blank=True)
    working_hours = models.CharField(max_length=100, blank=True)
    contact_email = models.EmailField(max_length=100, blank=True)
    contact_phone = models.CharField(max_length=10, blank=True, validators=[RegexValidator(r'^\d{10}$', 'Enter a 10-digit phone number.')])
    picture = models.ImageField(upload_to='static/images')
    map_url = models.URLField(blank=True)
    background_image = models.ImageField(upload_to='static/images', default='yange.jpg')  # New field for background image

    def __str__(self):
        return self.name

    
class CustomerRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=10, 
        blank=True, 
        validators=[RegexValidator(r'^\d{10}$', 'Enter a 10-digit phone number.')]
    )
    email = models.EmailField(max_length=100, blank=True)
    national_id_number = models.CharField(max_length=20, blank=True)
    amount_to_invest = models.DecimalField(max_digits=10, decimal_places=2, default=10000)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.full_name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
    
class District(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Ward(models.Model):
    ward_name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.ward_name

class Street(models.Model):
    street_name = models.CharField(max_length=255)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE) 

    def __str__(self):
        return self.street_name