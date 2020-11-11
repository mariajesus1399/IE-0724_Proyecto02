from django.db import models


GENDERS = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('U', 'Unknown')
]
SCHEDULE = [
    ('9:00', '9:00'),
    ('10:00', '10:00'),
    ('11:00', '11:00'),
    ('12:00', '12:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00')
]

class Pet(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDERS)
    age = models.PositiveIntegerField(blank=True)
    species = models.CharField(max_length=20)

class User(models.Model):
    mail = models.EmailField(max_length = 254) 
    password = models.CharField(max_length=30) # Change to diferent field
    name = models.CharField(max_length=30)

class Appointment(models.Model):
    date = models.DateField(null=True)
    provider = models.CharField(max_length=30) 
    client = models.CharField(max_length=30)
    hour = models.CharField(max_length=5, choices=SCHEDULE, default='0:00')
    
    class Meta:
        unique_together = ['date', 'provider', 'hour']