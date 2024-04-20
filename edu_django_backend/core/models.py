from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, email, phone_number, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        if not phone_number:
            raise ValueError(_("The phone number must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email,phone_number = phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, phone_number, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, phone_number, password, **extra_fields)


class User(AbstractUser):
    """
    Custom user model that supports using email instead of username
    """
    username = None
    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(verbose_name=_("phone number"),max_length=20,unique= True, help_text='Enter phone number')

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    def __str__(self):
        return self.email


