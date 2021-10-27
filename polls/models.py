from django.db import models
from phone_field import PhoneField
from django_countries.fields import CountryField


class Peoples(models.Model):
    dept_choices = (('SPECIAL', 'special'), ('NORMAL', 'normal'))

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='images', blank=True)
    department = models.CharField(max_length=15, choices=dept_choices, default="Normal", blank=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    country = CountryField(blank=True, null=True)
    address1 = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    address3 = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.first_name
