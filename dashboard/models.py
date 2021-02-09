from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    district = models.CharField(max_length=150)
    village = models.CharField(max_length=250)

    OCCUPATION_CHOICES = (
        ('Teacher', 'Teacher'),
        ('Nurse', 'Nurse'),
        ('Farmer', 'Farmer'),
        ('House Wife', 'House Wife'),
        ('Technician', 'Technician'),
        ('Student', 'Student'),

    )
    occupation = models.CharField(max_length=100, choices=OCCUPATION_CHOICES)



