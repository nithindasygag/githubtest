from django.forms import ModelForm
from .models import Peoples


class PeopleForm(ModelForm):
    class Meta:
        model = Peoples
        fields = '__all__'
