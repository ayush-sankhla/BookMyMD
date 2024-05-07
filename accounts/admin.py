from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(custom_user)
admin.site.register(Email_tokens)
admin.site.register(Doctor_Profile)
admin.site.register(Staff)
admin.site.register(Appointments)