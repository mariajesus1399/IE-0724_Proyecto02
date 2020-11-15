from django import forms
from .models import Pet
from .models import Appointment
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Extendemos del original
class AFWithEmail(AuthenticationForm):
    # Ahora el campo username es de tipo email y cambiamos su texto
    username = forms.EmailField(label="Username (email address)")

    class Meta:
        model = User
        fields = ["username", "password"]

# Extendemos del original
class UCFWithEmail(UserCreationForm):
    # Ahora el campo username es de tipo email y cambiamos su texto
    username = forms.EmailField(label="Email address")

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

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
