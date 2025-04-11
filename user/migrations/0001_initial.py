# Generated by Django 4.2.20 on 2025-04-11 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('mobile_no', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('OTHER', 'OTHER')], default='M', max_length=10)),
                ('dob', models.DateTimeField()),
                ('zodiac_sign', models.CharField(choices=[('Aries', 'Aries'), ('Taurus', 'Taurus'), ('Gemini', 'Gemini'), ('Cancer', 'Cancer'), ('Leo', 'Leo'), ('Virgo', 'Virgo'), ('Libra', 'Libra'), ('Scorpio', 'Scorpio'), ('Sagittarius', 'Sagittarius'), ('Capricorn', 'Capricorn'), ('Aquarius', 'Aquarius'), ('Pisces', 'Pisces')], default='Aries', max_length=30)),
                ('birth_place', models.CharField(max_length=50)),
                ('wallet_balance', models.FloatField()),
                ('is_customer', models.BooleanField()),
                ('is_astrologer', models.BooleanField()),
            ],
        ),
    ]
