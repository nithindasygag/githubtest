from rest_framework import serializers, fields
from .models import Peoples
from django_countries.serializers import CountryFieldMixin


class PeoplesSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Peoples
        fields = '__all__'