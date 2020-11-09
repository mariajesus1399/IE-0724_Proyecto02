from django import forms
from .models import Pet
from .models import Appointment

class PetForm(forms.ModelForm):
    
    class Meta:
        model = Pet
        fields = [
            'name',
            'gender',
            'age',
            'species',
        ]
        labels = {
            'name': 'Name',
            'gender': 'Gender',
            'age': 'Age',
            'species': 'Species',
        }

class AppointmentForm(forms.ModelForm) :
    class Meta:
        model = Appointment
        fields = [
            'date',
            'provider',
            'client',
            'hour',
        ]
        labels = {
            'date': 'Date [YYYY-MM-DD]',
            'hour': 'Hour',
            'provider': 'Provider',
            'client': 'Client',
        }
