from accounts.models import Doctor_Profile
from django.contrib.auth.hashers import check_password


def doctor_authenticate(email, password) :
    try:
        user = Doctor_Profile.objects.filter(email = email).first()

        hashed_password = user.password
        
        is_valid_password = check_password(password, hashed_password)

        if is_valid_password :
            return user
        else:
            return None
    except :
        pass

    return None



def doctor_document_result (user):
    if user.is_confirmed == True:
        return True
        
    else:
        return False