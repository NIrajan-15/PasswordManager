from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager ,PermissionsMixin
from django.utils.translation import gettext_lazy as _

# A custom Usermodel to represent User Manager
class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self,email,password, **extra_fields):
        if not email:
            raise ValueError(_("Your must provide an email address"))
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')
        
        return self.create_user(email,password,**extra_fields)



# A class representing User
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    
    start_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff=models.BooleanField(_('is_staff'), default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    


# A class representing Accounts 
class Account(models.Model):
    Account_choices = (('Kennedy Rice Mill','Kennedy Rice Mill'),('Neighbor Cookies','Neighbor Cookies'),)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    last_changed = models.DateTimeField(auto_now=True)
    bussiness = models.CharField(max_length=20, null=True, choices=Account_choices)
    description = models.CharField(max_length=500, null=True)
    
    def __str__(self):
        return self.name

# Class representing Update Hisotry 
class UpdateHistory(models.Model):
    email = models.EmailField(blank=True,null=True)
    updated_column = models.CharField(max_length=200,blank=True,null=True)
    updated_on = models.DateTimeField(default=timezone.now)
    updated_to = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.email