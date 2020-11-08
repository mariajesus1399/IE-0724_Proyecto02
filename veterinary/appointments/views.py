from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Pet
from .models import Appointment
from .forms import PetForm
from .forms import AppointmentForm

def home(request, pk=None):
    return HttpResponse('Showing "new" page')



def show(request, pk=None):
    if pk is not None:
        try:
            pet = Pet.objects.get(pk=pk)
        except Pet.DoesNotExist:
            raise Http404('Pet with pk {} doesn\'t exist!!!'.format(pk))

        return render(
            request,
            'show.html',
            {
                'object_pk': pet.pk,
                'object_name': pet.name,
                'object_age': pet.age,
            }
        )

    else:
        # Create a metadata dictionary
        pet_dict = {}
        for pet in Pet.objects.all():
            pet_dict[pet.name] = {
                'pk': pet.pk,
                'age': pet.age,
            }

        return render(
            request,
            'show.html',
            {
                'pet_dict': pet_dict,
            }
        )

def show_appointments(request, pk=None):
    if pk is not None:
        try:
            ap = Appointment.objects.get(pk=pk)
        except ap.DoesNotExist:
            raise Http404('Appointment with pk {} doesn\'t exist!!!'.format(pk))

        return render(
            request,
            'show_appointments.html',
            {
                'object_pk': ap.pk,
                'object_client': ap.client,
                'object_provider': ap.provider,
                'object_date': ap.date,
            }
        )
    else:
        # Create a metadata dictionary
        appointment_dict = {}
        for ap in Appointment.objects.all():
             appointment_dict[ap.client] = {
                'pk': ap.pk,
                'provider': ap.provider,
                'date': ap.date,
            }
        return render(
            request,
            'show_appointments.html',
            {
                'appointment_dict': appointment_dict,
            }
        )

def new(request):
    new_form = PetForm()
    if request.method == 'POST':
        filled_form = PetForm(request.POST)

        if filled_form.is_valid():
            new_pet = filled_form.save()
            note = (
                'Pet object with pk: \'{}\' was successfully created!!!\n'
                'Name: {}'.format(
                    new_pet.pk, filled_form.cleaned_data['name']
                )
            )
        else:
            note = 'INVALID!!!'
        return render(
            request,
            'new.html',
            {
                'petform': filled_form,
                'note': note
            }
        )
    else:
        return render(
            request,
            'new.html',
            {
                'petform': new_form,
            }
        )

def new_appointment(request):
    new_form = AppointmentForm()
    if request.method == 'POST':
        filled_form = AppointmentForm(request.POST)
        if filled_form.is_valid():
            new_ap = filled_form.save()
            note = (
                'Appointment with provider: \'{}\' was successfully created\n'
                'for client: {}'.format(
                    new_ap.provider, filled_form.cleaned_data['client']
                )
            )
        else:
            note = 'Invalid appointment'
        return render(
            request,
            'new_appointment.html',
            {
                'appointmentform': filled_form,
                'note': note
            }
        )
    else:
        return render(
            request,
            'new_appointment.html',
            {
                'appointmentform': new_form,
            }
        )
  