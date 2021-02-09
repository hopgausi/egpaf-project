from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Patient
from .forms import PatientForm


@login_required
def dashboard(request):
    context = {
        'title': 'Dashboard'
    }
    template_name = 'dashboard/index.html'
    return render(request,template_name, context)

@login_required
def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            form.save()
            messages.success(request, f'Patient {first_name} created, Create another Patient')
            return redirect('create_patient')
    else:
        form = PatientForm()
    context = {
        'form': form,
        'title': 'Create Patient',
    }
    template_name = 'dashboard/create_patient.html'
    return render(request,template_name, context)


@login_required
def patient_list(request):
    patients = Patient.objects.all()
    context = {
        'patients': patients,
        'title': 'Patients',
    }
    template_name = 'dashboard/patient_list.html'
    return render(request,template_name, context)