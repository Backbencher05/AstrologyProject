from django.contrib import admin
from user.models import UserModel
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'password', 'mobile_no', 'gender', 'dob', 
                    'zodiac_sign', 'birth_place', 'wallet_balance', 'is_customer', 'is_astrologer']

admin.site.register(UserModel, UserAdmin)