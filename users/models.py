from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils import timezone



class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                           **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, True, False, 
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, True, True,
                                 **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    member_type = [('EDUCATOR', 'educator'), ('ORGANIZATION','organization'), ('STUDENT', 'student')]
    gender_options = [('M', 'Male'), ('F', 'Female')]
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    birth_date = models.DateTimeField(blank=True, null=True)

 
    # profile_image = models.ImageField(null=True)
    cities_options = [('AMMAN', 'Amman'), ('ZARQA', 'Zarqa'), ('IRBID', 'Irbid'), ('MAFRAQ', 'Mafraq'), ('SALT', 'Salt'), ('MADABA', 'Madaba'),('AQABA', 'Aqaba'), ('MA`AN', 'Ma`an'), ('JARASH', 'Jarash'), ('AJLUN', 'Ajlun'), ('KARAK', 'Karak'), ('TAFILAH', 'Tafilah')]
    local = models.BooleanField(default="False")
    city = models.CharField(max_length=255, choices=cities_options, blank=True, null=True)
    member = models.CharField(max_length=255, choices=member_type, blank=True, null=True)
    organization_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=gender_options, blank=True, null=True)
    mobile_number = models.CharField( max_length=10, blank=True, null=True)
    specialization = models.CharField(max_length=255, blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    current_organization = models.CharField(max_length=255,blank=True, null=True)
    organization_summary = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    freelancer = models.BooleanField(default=False)
    hourly_tutoring_rate = models.IntegerField( blank=True, null=True)
    services = models.TextField( blank=True, null=True)
    updated_at = models.DateTimeField( blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]