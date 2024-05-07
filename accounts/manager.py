from django.contrib.auth.base_user import BaseUserManager

class UserManager (BaseUserManager) :

    def create_user (self, email, password = None, **otherfields) :
        if not email :
            raise ValueError("Please provide Email")
        
        email = self.normalize_email(email)
        
        user = self.model(email = email, **otherfields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser (self, email, password = None, **otherfields) :
        otherfields.setdefault('is_staff', True)
        otherfields.setdefault('is_superuser', True)
        otherfields.setdefault('is_active', True)

        return self.create_user(email, password, **otherfields)