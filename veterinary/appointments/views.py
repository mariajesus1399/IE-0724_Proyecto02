from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pet
from .models import Appointment
from .forms import PetForm
from .forms import AppointmentForm
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm

def delete(request, pk=None):
    # Recuperamos la instancia de la persona y la borramos
    if pk != None:
        instancia = Appointment.objects.get(id=pk)
        instancia.delete()
    # Después redireccionamos de nuevo a la lista
    return redirect('/show_appointments')

def edit(request, pk=None):
    # Recuperamos la instancia de la persona
    try:
        instancia = Appointment.objects.get(id=pk)
    except Appointment.DoesNotExist:
        raise Http404('pk no existe')

    if pk != None:
        # Creamos el formulario con los datos de la instancia
        form = AppointmentForm(instance=instancia)

        # Comprobamos si se ha enviado el formulario
        if request.method == "POST":
            # Actualizamos el formulario con los datos recibidos
            form = AppointmentForm(request.POST, instance=instancia)
            # Si el formulario es válido...
            if form.is_valid():
                # Guardamos el formulario pero sin confirmarlo,
                # así conseguiremos una instancia para manejarla
                instancia = form.save(commit=False)
                # Podemos guardarla cuando queramos
                instancia.save()
                note = 'exito'
                # exito y redigir con render
        else:
            note = ''
    else:
        raise Http404('Necesita pk')
    # Si llegamos al final renderizamos el formulario
    return render(request, "edit.html", {'form': form, 'note':note})

def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "welcome.html")
    # En otro caso redireccionamos al login
    return redirect('/login')

def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/welcome')

    # Si llegamos al final renderizamos el formulario
    # Si queremos borramos los campos de ayuda
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    return render(request, "register.html", {'form': form})

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/welcome')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/login')

def home(request, pk=None):
    #return HttpResponse('Showing "new" page')
    return render(request, "start.html")

def welcome_admin(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "welcome_admin.html")
    # En otro caso redireccionamos al login
    return redirect('/login_admin')

def register_admin(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/welcome_admin')

    # Si llegamos al final renderizamos el formulario
    # Si queremos borramos los campos de ayuda
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    return render(request, "register_admin.html", {'form': form})

def login_admin(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/welcome_admin')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login_admin.html", {'form': form})

def logout_admin(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/login_admin')

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
