from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.core.exceptions import ValidationError


def validate_edu_email_address(email):
    if not email.endswith('.edu'):
        raise forms.ValidationError("Only .edu email addresses allowed")


class Studentuser(AbstractUser):
    email = models.EmailField(verbose_name='email',
                              max_length=255, unique=True, validators=[validate_edu_email_address])
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
