from django.core.mail import send_mail
from django.conf import settings

def verification_rejection_mail (name, email, reason) :
    subject = 'Verification Failed!'
    message = f'Hi {name}, Your Account verification is failed due to {reason}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def send_token_via_mail (email, token):
    subject = "Verify your account"
    message = f"Hi http://localhost:8000/verify/{token}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def send_appointment_booking_success (email, name, doctor_name, date, clinic_name, clinic_address, clinic_number) :
    subject = 'Appointment booking request received'
    message = f"Dear {name},\n\nThank you for using BookMyMD for appointment booking with Dr. {doctor_name} at {clinic_name}.\n\n\nWe have received your appointment request and are currently processing it. Your appointment status is pending from Dr. {doctor_name}. Once confirmed by the doctor, you will receive a notification along with any additional instructions, if necessary.\n\nHere are the details of your appointment: \n- Doctor's Name: Dr. {doctor_name}\n- Date: {date}\n-Clinic Address: {clinic_address} - Clinic Contact Number: {clinic_number}\nPlease note that your appointment is not yet confirmed. We will notify you as soon as it is confirmed by the doctor.\n\nIf you have any questions or need further assistance, please don't hesitate to contact us to this email.\n\nThank you for using BookMyMD. We appreciate your trust in our platform.\n\nBest regards, \nBookMyMD"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


