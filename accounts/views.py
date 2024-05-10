from django.shortcuts import render, redirect
from django.http import request, HttpResponseRedirect, HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
import uuid
from django.conf import settings
from django.core.mail import send_mail
from accounts.doctor_authentication import *
from accounts.mail import *




# Create your views here.


@login_required(login_url='/login')
def user_home(request) :

    token = Email_tokens.objects.filter(user = request.user).first()

    userid = token.auth_token

    Appointment_obj = Appointments.objects.filter(user_id = userid)[:5]

    return render(request, 'user_home.html', {'data': Appointment_obj})


def User_Login(request) :

    if request.method == "POST" :
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = custom_user.objects.filter(email = email).first()

        if user_obj is None :
            messages.success(request, "User not found!")
            return redirect('/login')
        
        email_token_obj = Email_tokens.objects.filter(user = user_obj).first()
        
        user = authenticate(email = email, password = password)

        if user is None :
            messages.success(request, "Wrong Password")
            return redirect('/login')
        
        if not email_token_obj.is_verified :
            messages.success(request, "Email is not verified! Please check your mail..")
            return redirect('/login')
    
        login(request, user)        
        
        return redirect('/user/home/')

    return render(request, 'user_login.html')


def User_Register(request) :

    try :
        if request.method == 'POST' :
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            cpassword = request.POST.get('cpassword')

            if custom_user.objects.filter(email = email).first() or Doctor_Profile.objects.filter(email = email).first() :
                messages.success(request, "Email is already taken")
                return redirect("/register")
            
            if password != cpassword :
                messages.success(request, "Password are not same")
                return redirect("/register")
            
            token = str(uuid.uuid4())
            
            user_obj = custom_user.objects.create(full_name = name, email = email)
            user_obj.set_password(password)

            email_token_obj = Email_tokens.objects.create(user = user_obj, auth_token = token)
            email_token_obj.save()
            user_obj.save()

            send_token_via_mail(email, token)

            url = f'/email_verification/sent?email={email}'
            return HttpResponseRedirect(url)

    except Exception as e :
        print(e)

    return render(request, 'user_registration.html')


@login_required(login_url='/login')
def logout_user(request) :
    if request.method == "POST":
        logout(request)
        return redirect ('/login')


def Doctor_Login(request):

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = Doctor_Profile.objects.filter(email = email).first()

        if user_obj is None :
            messages.success(request, "User not found!")
            return redirect('/doc_login')

        user = doctor_authenticate(email, password)

        if user is None :
            messages.success(request, "Wrong Password")
            return redirect('/doc_login')
        
        if not user.is_verified :
            messages.success(request, "Email is not verified! Please check your mail..")
            return redirect('/doc_login')
        
        if not doctor_document_result(user):
            return redirect('/doctor_verification_pending/')
        
        return redirect('/doc/dashboard/{}'.format(user.auth_token))

    return render(request, 'doctor_login.html')



def Doctor_Register(request) :

    try :
        if request.method == 'POST' :

            full_name = request.POST.get('full_name')
            dob = request.POST.get('dob')
            father_name = request.POST.get('father_name')
            gender = request.POST.get('gender')
            degree = request.POST.get('degree')
            specialist = request.POST.get('specialist')
            email = request.POST.get('email')
            mob_number = request.POST.get('mob_number')
            clinic_number = request.POST.get('clinic_number')
            add_line_1 = request.POST.get('add_line_1')
            add_line_2 = request.POST.get('add_line_2')
            landmark = request.POST.get('landmark')
            city = request.POST.get('city')
            state = request.POST.get('state')
            pincode = request.POST.get('pincode')
            hospital_name = request.POST.get('hospital_name')
            hospital_address = request.POST.get('hospital_address')
            hospital_state = request.POST.get('hospital_state')
            hospital_pincode = request.POST.get('hospital_pincode')
            fees = request.POST.get('fees')
            experience = request.POST.get('experience')
            days_available = request.POST.get('days_available')
            bio = request.POST.get('bio')
            reg_number = request.POST.get('reg_number')
            degree_upload = request.POST.get('degree_upload')
            profile_picture = request.POST.get('profile_picture')
            password = request.POST.get('password')
            cpassword = request.POST.get('cpassword')

            if (custom_user.objects.filter(email = email).first()) or (Doctor_Profile.objects.filter(email = email).first()) :
                messages.success(request, "Email is already available")
                return redirect("/doc_register")
            
            if password != cpassword :
                messages.success(request, "Password are not same")
                return redirect("/doc_register")

            token = str(uuid.uuid4())
 
            doctor_register_obj = Doctor_Profile.objects.create(
                full_name = full_name,
                dob = dob,
                father_name = father_name,
                gender = gender,
                degree = degree,
                specialist = specialist,
                email = email,
                mob_number = mob_number,
                clinic_number = clinic_number,
                add_line_1 = add_line_1,
                add_line_2 = add_line_2,
                landmark = landmark,
                city = city,
                state = state,
                pincode = pincode,
                hospital_name = hospital_name,
                hospital_address = hospital_address,
                hospital_state = hospital_state,
                hospital_pincode = hospital_pincode,
                fees = fees,
                experience = experience,
                days_available = days_available,
                bio = bio,
                reg_number = reg_number,
                degree_upload = degree_upload,
                profile_picture = profile_picture,
                password = make_password(password),
                auth_token = token
            )            

            doctor_register_obj.save()
            
            send_token_via_mail(email, token)

            url = f'/email_verification/sent?email={email}'
            return HttpResponseRedirect(url)

    except Exception as e :
        print(e)

    return render(request, 'doctor_register.html')

@login_required(login_url='/doc_login')
def logout_doctor(request) :
    if request.method == "POST":
        logout(request)
        return redirect ('/doc_login')


def Email_Verification(request):
    if request.method == 'GET':
        email = request.GET.get('email')
    return render(request, 'email_verification.html', {'email' : email})


def Email_Verification_Success(request):
    return render(request, 'email_verification_success.html')


def verify(request, token):

    try :

        email_token_obj = Email_tokens.objects.filter(auth_token = token).first()
        email_token_obj_2 = Doctor_Profile.objects.filter(auth_token = token).first()

        if email_token_obj :

            if email_token_obj.is_verified == True :
                messages.success(request, "Profile is already verified!")
                return redirect('/email_verification/success')
            
            email_token_obj.is_verified = True
            email_token_obj.save()
            return redirect('/email_verification/success')
        
        if email_token_obj_2 :

            if email_token_obj_2.is_verified == True :
                messages.success(request, "Profile is already verified!")
                return redirect('/email_verification/success')
            
            email_token_obj_2.is_verified = True
            email_token_obj_2.save()
            return redirect('/email_verification/success')


    except Exception as e:
        print(e)

# @login_required(login_url='/doc_login')
def Doctor_dashboard(request, user) :

    # user = request.GET.get('user')

    Doctor_Profile_obj = Doctor_Profile.objects.get(auth_token = user)
    Appointment_obj = Appointments.objects.filter(doctor = user)[:5]
    Appointment_count = Appointment_obj.count()
    Pending_appointment = Appointments.objects.filter(doctor = user,status = 'Pending')
    Pending_appointment_count = Pending_appointment.count()
    Confirmed_appointment = Appointments.objects.filter(doctor = user,status = 'Confirmed')
    Confirmed_appointment_count = Confirmed_appointment.count()

    data = {
        'Doctor_Profile_obj' : Doctor_Profile_obj,
        'Appointments' : Appointment_obj,
        'Total' : Appointment_count,
        'Pending_appointment' : Pending_appointment,
        'Pending_appointment_count' : Pending_appointment_count,
        'Confirmed_appointment' : Confirmed_appointment,
        'Confirmed_appointment_count' : Confirmed_appointment_count
    }

    return render(request, 'doc_home.html', data)

def Doctor_Verification_Pending(request):
    return render(request, 'doctor_verification_pending.html')

@login_required(login_url='/staff/login')
def Staff_Home (request) :

    Doctor_Profile_obj = Doctor_Profile.objects.filter(is_confirmed = False).values_list('profile_picture','full_name', 'degree', 'city', 'specialist', 'auth_token')
    Pending_Profile_Count = Doctor_Profile.objects.filter(is_confirmed = False).count()
    Confirmed_Doctor = Doctor_Profile.objects.filter(is_confirmed = True).count()
    Total_Count = Pending_Profile_Count + Confirmed_Doctor

    data = {
        'Doctor_Profile_obj' : Doctor_Profile_obj,
        'Pending_Profile_Count' : Pending_Profile_Count,
        'Confirmed_Doctor' : Confirmed_Doctor,
        'Total_Count' : Total_Count
    }

    return render(request, 'staff_home.html', data)

def Staff_Login(request) :

    if request.method == "POST" :
        uid = request.POST.get('uid')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = custom_user.objects.filter(email = email).first()

        if user_obj is None :
            messages.success(request, "User not found!")
            return redirect('/staff/login')
        
        staff_obj = Staff.objects.filter(uid = uid).first()

        if staff_obj is None :
            messages.success(request, "Invalid User ID")
            return redirect('/staff/login')
        
        user = authenticate(email = email, password = password)

        if user is None :
            messages.success(request, "Wrong Password")
            return redirect('/staff/login')
    
        login(request, user)        
        
        return redirect('/staff/home')

    return render(request, 'staff_login.html')


@login_required(login_url='/staff/login')
def logout_staff(request) :
    if request.method == "POST":
        logout(request)
        return redirect ('/staff/login')
    

@login_required(login_url='/staff/login')
def Staff_Doctor_Profile(request, id) :

    Doctor_Profile_obj = Doctor_Profile.objects.filter(auth_token = id).first()

    data = {
        'Doctor_Profile_obj' : Doctor_Profile_obj
    }

    return render(request, 'staff_doctor_profile.html', data)


@login_required(login_url='/staff/login')
def Staff_Doctor_Verified(request, id) :
    
    Doctor_Profile.objects.filter(auth_token = id).update(is_confirmed = True)

    return render (request, 'Doctor_Verified.html')

@login_required(login_url='/staff/login')
def Staff_Doctor_Reject(request, id) :
    
    if request.method == 'POST' :

        reason = request.POST.get('reason')

        Doctor_obj = Doctor_Profile.objects.filter(auth_token = id).first()

        if Doctor_obj is None :
            messages.success(request, "Invalid Id")
            return redirect ('/staff/home')
        
        verification_rejection_mail(Doctor_obj.full_name, Doctor_obj.email, reason)

        Doctor_obj.delete()

        return redirect ('/staff/home')

    return render(request, 'doctor_verification_reject.html')

def Staff_Verification_Pending(request) :

    Doctor_Profile_obj = Doctor_Profile.objects.filter(is_confirmed = False).values_list('profile_picture','full_name', 'degree', 'city', 'specialist', 'auth_token')

    data = {
        'Doctor_Profile_obj' : Doctor_Profile_obj
    }

    return render(request, 'staff_verification_pending.html', data)


def search_doctor(request) :

    if request.method == "GET" :
        name = request.GET.get ('name')
        city = request.GET.get ('city')
        speciality = request.GET.get ('speciality')

        if name and city :
            Doctor_Profile_obj = Doctor_Profile.objects.filter(full_name__startswith = name, city__startswith = city, is_confirmed = True)
        
        elif name and speciality :
            Doctor_Profile_obj = Doctor_Profile.objects.filter(full_name__startswith = name, specialist__startswith = speciality, is_confirmed = True)

        elif city and speciality :
            Doctor_Profile_obj = Doctor_Profile.objects.filter(city__startswith = city, specialist__startswith = speciality, is_confirmed = True)
        
        elif name and city and speciality :
            Doctor_Profile_obj = Doctor_Profile.objects.filter(full_name__startswith = name, city__startswith = city, specialist__startswith = speciality, is_confirmed = True)

        elif name :
            Doctor_Profile_obj = Doctor_Profile.objects.filter(full_name__startswith = name, is_confirmed = True)
            
        elif city :
            Doctor_Profile_obj = Doctor_Profile.objects.filter(city__startswith = city, is_confirmed = True)

        elif speciality :
            Doctor_Profile_obj = Doctor_Profile.objects.filter(specialist__startswith = speciality, is_confirmed = True)

        else:
            messages.success(request, "No similar results")
            return redirect("/user/home/")

        if len(Doctor_Profile_obj) == 0 :
            messages.success(request, "No similar results")
            return redirect("/user/home/")
        
        data = {
            'result' : Doctor_Profile_obj
        }
        
        return render(request, 'search_doctor.html', data)

    return redirect("/user/home/")

@login_required(login_url='/login')
def User_Appointment(request) :

    token = Email_tokens.objects.filter(user = request.user).first()

    userid = token.auth_token

    Appointment_obj = Appointments.objects.filter(user_id = userid)

    return render(request, 'user_all_appointments.html', {'data': Appointment_obj})


@login_required(login_url='/login/')
def Appointment_Booking (request, id) :
    
    Doctor_Profile_obj = Doctor_Profile.objects.filter(auth_token = id).first()

    if Doctor_Profile_obj is None :
        messages.success(request, 'Something went wrong!')
        return redirect("/user/home")
    
    return render(request, 'user_doctor_profile.html', {'Doctor_Profile_obj': Doctor_Profile_obj})


@login_required(login_url='/login')
def Appointment_Pending(request) :

    if request.method == 'GET' :

        email = request.user.email
        id = request.GET.get('id')
        name = request.GET.get('name')
        date = request.GET.get('appointment_date')
        num = request.GET.get('number')
        alt_num = request.GET.get('alt_number')

        unique_id = str(uuid.uuid4())

        user_obj = custom_user.objects.filter(email = email).first()
        doctor_profile_obj = Doctor_Profile.objects.filter(auth_token = id).first()

        if user_obj is None :
            return redirect ('/login/')
        
        if doctor_profile_obj is None :
            return HttpResponse("Something went wrong!")
        
        token_obj = Email_tokens.objects.filter(user = user_obj).first()
        userid = token_obj.auth_token

        appointment_obj = Appointments.objects.filter(user_id = userid, appointment_date = date)

        print('date',date)
        if appointment_obj is not None :
            for value in appointment_obj :
                if value.doctor == id:
                    return HttpResponse(f"Appointment already book for {date} with Dr. {doctor_profile_obj.full_name}.\nPlease try with another date...")
   
        appointment_book_obj = Appointments.objects.create(user_id = userid, doctor = id,name = name ,appointment_date = date, number = num, alternate_num = alt_num, unique_id = unique_id)

        appointment_book_obj.save()

        doctor_name = doctor_profile_obj.full_name
        clinic_name = doctor_profile_obj.hospital_name
        clinic_address = doctor_profile_obj.hospital_address
        clinic_number = doctor_profile_obj.clinic_number
        name = user_obj.full_name

        data = {
            'doctor_name' : doctor_name
        }

        send_appointment_booking_success (email, name, doctor_name, date, clinic_name, clinic_address, clinic_number)

        return render(request, 'appointment_confirmation_pending.html', data)
    
    return redirect ('/user/home')


def Doctor_Appointments_Pending(request, user) :

    Doctor_Profile_obj = Doctor_Profile.objects.get(auth_token = user)
    Pending_appointment = Appointments.objects.filter(doctor = user,status = 'Pending')

    data = {
        'Doctor_Profile_obj' : Doctor_Profile_obj,
        'Pending_appointment' : Pending_appointment,
    }

    return render(request, 'doctor_all_appointments.html', data)

def Doctor_Appointments_confirmed (request, user) :

    Doctor_Profile_obj = Doctor_Profile.objects.get(auth_token = user)
    Confirmed_appointment = Appointments.objects.filter(doctor = user,status = 'Confirmed')

    data = {
        'Doctor_Profile_obj' : Doctor_Profile_obj,
        'Confirmed_appointment' : Confirmed_appointment,
    }

    return render (request, 'doctor_all_confirmed_appointments.html', data)

def Doctor_Appointments_Accept (request, user) :

    Doctor_Profile_obj = Doctor_Profile.objects.filter(auth_token = user).first()

    if Doctor_Profile_obj is None :
        HttpResponse("Something went wrong!")

    if request.method == "GET" :
        unique_id = request.GET.get('appointment')

        Appointment_obj = Appointments.objects.filter(unique_id = unique_id)

        if Appointment_obj is None :
            HttpResponse('No Appointment Found!')

        data = {
            'unique_id' : unique_id,
            'doctor' : Doctor_Profile_obj.auth_token
        }

        return render (request, 'Appointment_Time_Schedule.html', data)
    
    HttpResponse('Something went wrong!')

def Doctor_Appointments_Reject (request, user) :

    Doctor_Profile_obj = Doctor_Profile.objects.filter(auth_token = user).first()

    if Doctor_Profile_obj is None :
        HttpResponse("Something went wrong!")

    if request.method == "GET" :
        unique_id = request.GET.get('appointment')

        Appointment_obj = Appointments.objects.filter(unique_id = unique_id)

        if Appointment_obj is None :
            HttpResponse('No Appointment Found!')

        data = {
            'unique_id' : unique_id,
            'doctor' : Doctor_Profile_obj.auth_token
        }

        return render (request, 'appointment_reject_reason.html', data)
    
    HttpResponse('Something went wrong!')


def Doctor_Appointed_Accepted_Successfully(request) :
    if request.method == "POST" :
        
        id = request.POST.get('id')
        time = request.POST.get('time')
        doctor = request.POST.get('doctor')

        Appointments_obj = Appointments.objects.filter(unique_id = id).first()

        user_id = Appointments_obj.user_id

        email_obj = Email_tokens.objects.filter(auth_token = user_id).first()

        if Appointments_obj is None :
            HttpResponse('Something went wrong!')

        Appointments_obj.appointment_time = time
        Appointments_obj.status = 'Confirmed'
        Appointments_obj.save()

        Doctor_Profile_obj = Doctor_Profile.objects.filter(auth_token = doctor).first()

        send_appointment_confirmation_mail(email_obj.user, Appointments_obj.name, time, Doctor_Profile_obj.full_name)

        data = {
            'doctor' : Doctor_Profile_obj.auth_token
        }

        return render(request, 'appointment_successfully_accepted.html', data)
    
    HttpResponse('Something went wrong!')


def Doctor_Appointed_Rejected_Successfully(request):
    
    if request.method == "POST" :
        
        id = request.POST.get('id')
        reason = request.POST.get('reason')
        doctor = request.POST.get('doctor')

        Appointments_obj = Appointments.objects.filter(unique_id = id).first()

        user_id = Appointments_obj.user_id

        email_obj = Email_tokens.objects.filter(auth_token = user_id).first()

        if Appointments_obj is None :
            HttpResponse('Something went wrong!')

        Doctor_Profile_obj = Doctor_Profile.objects.filter(auth_token = doctor).first()

        send_appointment_rejection_mail(email_obj.user, Appointments_obj.name, reason, Doctor_Profile_obj.full_name)

        data = {
            'doctor' : Doctor_Profile_obj.auth_token
        }

        Appointments_obj.delete()

        return render(request, 'appointment_reject_success.html', data)
    
    HttpResponse('Something went wrong!')