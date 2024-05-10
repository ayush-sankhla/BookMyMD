from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.

class custom_user (AbstractUser):
    username = None
    first_name = None
    last_name = None
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, null=True)
    mobile_no = models.IntegerField(null=True)
    blood_group = models.CharField(max_length=5, null=True)
    add_line1 = models.CharField(max_length=100, null=True)
    add_line2 = models.CharField(max_length=100, null=True)
    landmark = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    pincode = models.IntegerField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


# Doctor Registration Model

class Doctor_Profile (models.Model) :

    full_name = models.CharField(max_length=100)
    dob = models.DateField(blank=True, null=True)
    father_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, null=True)
    degree = models.CharField(max_length=50)
    specialist = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mob_number = models.IntegerField(null=True)
    clinic_number = models.IntegerField(null=True)
    add_line_1 = models.CharField(max_length=100, null=True)
    add_line_2 = models.CharField(max_length=100, null=True)
    landmark = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    pincode = models.IntegerField(null=True)
    hospital_name = models.CharField(max_length=200, null=True)
    hospital_address = models.CharField(max_length=200)
    hospital_state = models.CharField(max_length=50, null=True)
    hospital_pincode = models.IntegerField(null=True)
    fees = models.IntegerField(null=True)
    experience = models.IntegerField(null=True, default=0)
    days_available = models.CharField(max_length=100)
    bio = models.CharField(max_length=300)
    reg_number = models.CharField(max_length=20)
    degree_upload = models.FileField(upload_to='Media/Media/Degree/', max_length=250, null=True, default=None)
    profile_picture = models.FileField(upload_to='Media/Media/Profile/', max_length=250, null=True, default=None)
    password = models.CharField(max_length=128)

    # For Email Verification
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    last_login = models.DateTimeField(blank=True, null=True)


# Email Verification Database

class Email_tokens(models.Model) :
    user = models.OneToOneField(custom_user, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


# Staff Model

class Staff(models.Model) :
    uid = models.IntegerField(unique=True)
    user = models.OneToOneField(custom_user, on_delete=models.CASCADE)


# Appointment Model

class Appointments (models.Model) :
    # user = models.OneToOneField(custom_user, on_delete= models.CASCADE, unique=False)
    unique_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    name = models.CharField(max_length=100, default='')
    appointment_date = models.DateField()
    appointment_time = models.CharField(max_length=100, default='Not Scheduled')
    number = models.IntegerField(default=1)
    alternate_num = models.IntegerField(default=1)
    status = models.CharField(max_length=10, default='Pending')
