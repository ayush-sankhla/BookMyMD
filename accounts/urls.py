from django.contrib import admin
from django.urls import path
from accounts import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('user/home/', views.user_home, name='User_Home'),
    path('user/home/search/', views.search_doctor, name='search_doctor'),
    path('user/appointment/', views.User_Appointment, name='User_Appointments'),
    path('user/book_appointment/doctor/<id>', views.Appointment_Booking, name='Appointment_Booking'),
    # path('user/book_appointment/confirm/', views.Appointment_Booking_Request, name='Appointment_Booking_Request'),
    path('user/appointment/pending/', views.Appointment_Pending, name='Appointment_Pending'),
    path('login/', views.User_Login, name='User_Login'),
    path('register/', views.User_Register, name='User_Register'),
    path('user/logout/', views.logout_user, name='Logout_User'),

    path('email_verification/sent', views.Email_Verification, name='Email_Verification'),
    path('email_verification/success', views.Email_Verification_Success, name='Email_Verification_Success'),
    path('doctor_verification_pending/', views.Doctor_Verification_Pending, name='Doctor_Verification_Pending'),
    path('verify/<token>', views.verify, name='verify'),

    path('doc/dashboard/<user>', views.Doctor_dashboard, name='Doc_Dashboard'),
    path('doc/appointments/pending/<user>', views.Doctor_Appointments_Pending, name='Doctor_Appointments_Pending'),
    path('doc/appointments/confirmed/<user>', views.Doctor_Appointments_confirmed, name='Doctor_Appointments_confirmed'),
    path('doc/appointments/accept/<user>/', views.Doctor_Appointments_Accept, name='Doctor_Appointments_Accept'),
    path('doc/appointments/reject/<user>/', views.Doctor_Appointments_Reject, name='Doctor_Appointments_Reject'),
    path('doc/appointment/success', views.Doctor_Appointed_Accepted_Successfully, name='Doctor_Accepted_Successfully'),
    path('doc/appointment/rejected', views.Doctor_Appointed_Rejected_Successfully, name='Doctor_Rejected_Successfully'),
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


urlpatterns += staticfiles_urlpatterns()