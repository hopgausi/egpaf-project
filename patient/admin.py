from django.contrib import admin
from .models import Patient, Assessment

admin.site.register(Patient)
admin.site.register(Assessment)