from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    is_seller = models.BooleanField(default=False)
    gender = models.CharField(max_length=50, choices=GENDER)
    account_balance = models.DecimalField(max_digits=8,decimal_places=2, blank=True, null=True, default=0.00)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email