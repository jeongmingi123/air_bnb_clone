from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other")
    )

    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    avatar = models.ImageField(default="", null=True)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=10, null=True, blank=True)
    bio = models.TextField(default="", null=True, blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, null=True)
    currency = models.CharField(choices=LANGUAGE_CHOICES, max_length=10, null=True, blank=True)
    superhost = models.BooleanField(default=False)
