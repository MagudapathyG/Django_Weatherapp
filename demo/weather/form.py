#default form creation in django so we used forms.py (modelform)

from django.forms import ModelForm,TextInput
from .models import City

class CityForm(ModelForm):
    class Meta: # meta is used to change the behavior of our model fields.
        model=City
        fields=["name"]
        widgets={'name':TextInput(attrs={'class':'form-control','placeholder':'City Name'})} #class and placeholder are attrs

#text input for create a input fields

