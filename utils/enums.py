from django.db import models
from django.utils.translation import gettext_lazy as _

class GenderChoices(models.TextChoices):
    MALE = 'M', _("Male")
    FEMALE = 'F', _("Female")
    OTHER = 'OTHER', _("OTHER")


class ZodiacChoices(models.TextChoices):
    Aries = 'Aries', _("Aries")
    Taurus = 'Taurus', _("Taurus")
    Gemini = 'Gemini', _("Gemini")
    Cancer = 'Cancer', _("Cancer")
    Leo = 'Leo', _("Leo")
    Virgo = 'Virgo', _("Virgo")
    Libra = 'Libra', _("Libra")
    Scorpio = 'Scorpio', _("Scorpio")
    Sagittarius = 'Sagittarius', _("Sagittarius")
    Capricorn = 'Capricorn', _("Capricorn")
    Aquarius = 'Aquarius', _("Aquarius")
    Pisces = 'Pisces', _("Pisces")
    