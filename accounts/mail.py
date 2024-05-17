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
    message = f"Dear User,\n\nThank you for registering with BookMyMD. To ensure that we have the correct email address and to activate your account, please confirm your email address by clicking on the link below:\n\nhttps://bookmymd.onrender.com/verify/{token}\n\nIf the above link does not work, please copy and paste the following URL into your web browser.\n\nPlease note that this link is valid for a limited time only.\nIf you did not register for an account with BookMyMD, please disregard this email. If you have any questions or concerns, please contact our support team.\n\nThank you for choosing BookMyMD.\n\nBest regards,\nBookMyMD"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def send_appointment_booking_success (email, name, doctor_name, date, clinic_name, clinic_address, clinic_number) :
    subject = 'Appointment booking request received'
    message = f"Dear {name},\n\nThank you for using BookMyMD for appointment booking with Dr. {doctor_name} at {clinic_name}.\n\n\nWe have received your appointment request and are currently processing it. Your appointment status is pending from Dr. {doctor_name}. Once confirmed by the doctor, you will receive a notification along with any additional instructions, if necessary.\n\nHere are the details of your appointment: \n- Doctor's Name: Dr. {doctor_name}\n- Date: {date}\n-Clinic Address: {clinic_address} - Clinic Contact Number: {clinic_number}\nPlease note that your appointment is not yet confirmed. We will notify you as soon as it is confirmed by the doctor.\n\nIf you have any questions or need further assistance, please don't hesitate to contact us to this email.\n\nThank you for using BookMyMD. We appreciate your trust in our platform.\n\nBest regards, \nBookMyMD"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def send_appointment_confirmation_mail(email, name, time, doctor) :
    
    subject = f"Appointment Confirmation: Your Appointment with Dr. {doctor} Confirmed"
    message = f"Dear {name}, \n\nWe are pleased to confirm your upcoming appointment with Dr. {doctor} through BookMyMD. \n\nAppointment Details:\n- Patient's Name: {name}\n- Doctor's Name: Dr. {doctor} \n- Appointment Time: {time}\n\nYour appointment is scheduled as requested. We kindly ask that you arrive promptly at least 10 minutes before your appointment time to ensure a smooth and efficient visit.\n\nShould you have any questions or need to make any adjustments to your appointment, please do not hesitate to reach out to us.\n\nThank you for entrusting BookMyMD with your healthcare needs. We look forward to providing you with excellent care.\n\nWarm regards,\nBookMyMD Team"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def send_appointment_rejection_mail(email, name, reason, doctor) :
    
    subject = f"Appointment Rejection Notification: {name} with Dr. {doctor}"
    message = f"Dear {name},\n\nWe regret to inform you that your appointment request with Dr. {doctor} has been rejected. Below is the reason provided by the doctor:\n\nReason for Rejection:\n{reason}\n\nWe apologize for any inconvenience this may cause. Should you require further assistance or wish to reschedule, please don't hesitate to contact us.\n\nThank you for your understanding.\n\nBest regards,\nBookMyMD Team"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


