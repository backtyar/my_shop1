from django.db import models

from django.contrib.auth.models import AbstractBaseUser

from .manager import CustomUserManager


class CustomUser(AbstractBaseUser):
    pass