from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    # unique=True - bir xil raqam bilan ikki marta ro'yxatdan o'tib bo'lmaydi
    # blank=False va null=False - raqam yozish majburiy
    telephone_number = models.CharField(
        max_length=20, 
        unique=True, 
        null=False, 
        blank=False,
        verbose_name="Telefon raqami"
    )
