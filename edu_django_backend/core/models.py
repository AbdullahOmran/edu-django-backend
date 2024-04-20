from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    pass


class User(AbstractUser):
    """
    Custom user model that supports using email instead of username
    """
    username = None
    name = models.CharField(
        _("name"),
        max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
    )
    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(max_length=20,unique= True, help_text='Enter phone number')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()


