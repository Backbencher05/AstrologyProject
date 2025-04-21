from django.db import models
from utils.enums import *

# Create your models here.
class UserModel(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    mobile_no = models.IntegerField()
    gender = models.CharField(choices=GenderChoices.choices, default=GenderChoices.MALE, max_length=10)
    dob = models.DateTimeField()
    zodiac_sign = models.CharField(max_length=30, choices=ZodiacChoices.choices, default=ZodiacChoices.Aries)
    birth_place = models.CharField(max_length=50)
    wallet_balance = models.FloatField()
    is_customer = models.BooleanField()
    is_astrologer = models.BooleanField()

    def __str__(self):
        return super().__str__()

