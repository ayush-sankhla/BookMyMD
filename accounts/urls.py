from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [

    path('user/home/', views.user_home, name='User_Home'),
    path('user/home/search/', views.search_doctor, name='search_doctor'),
    path('user/appointment/', views.User_Appointment, name='User_Appointments'),
    path('user/book_appointment/<id>', views.Appointment_Booking, name='Appointment_Booking'),
    path('user/appointment/pending/', views.Appointment_Pending, name='Appointment_Pending'),
    path('login/', views.User_Login, name='User_Login'),
    path('register/', views.User_Register, name='User_Register'),
    path('user/logout/', views.logout_user, name='Logout_User'),

    path('email_verification/sent', views.Email_Verification, name='Email_Verification'),
    path('email_verification/success', views.Email_Verification_Success, name='Email_Verification_Success'),
    path('doctor_verification_pending/', views.Doctor_Verification_Pending, name='Doctor_Verification_Pending'),
    path('verify/<token>', views.verify, name='verify'),

    path('doc/dashboard/', views.Doctor_dashboard, name='Doc_Dashboard'),
    path('doc_login/', views.Doctor_Login, name='Doctor_Login'),
    path('doc_register/', views.Doctor_Register, name='Doc_Register'),
    path('doctor/logout/', views.logout_doctor, name='Logout_Doctor'),


    path('staff/home', views.Staff_Home, name='Staff_Home'),
    path('staff/home/verification/pending', views.Staff_Verification_Pending, name='Staff_Verification_Pending'),
    path('staff/login', views.Staff_Login, name='Staff_Login'),
    path('staff/logout/', views.logout_staff, name='Logout_Staff'),
    path('staff/doctor/profile/<id>', views.Staff_Doctor_Profile, name='Staff_Doctor_Profile'),
    path('staff/doctor/accept/<id>', views.Staff_Doctor_Verified, name='Staff_Doctor_Verified'),
    path('staff/doctor/reject/<id>', views.Staff_Doctor_Reject, name='Staff_Doctor_Reject'),



]
