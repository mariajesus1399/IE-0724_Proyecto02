from django.db import models


GENDERS = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('U', 'Unknown')
]


class Pet(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDERS)
    age = models.PositiveIntegerField(blank=True)
    species = models.CharField(max_length=20)

class User(models.Model):
    mail = models.EmailField(max_length = 254) 
    password = models.CharField(max_length=30) #Change to diferent field
    name = models.CharField(max_length=30)

class Appointment(models.Model):
    date = models.CharField(max_length=30)  
    provider = models.CharField(max_length=30) #Change to diferent field
    client = models.CharField(max_length=30)