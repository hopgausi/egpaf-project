from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib import messages
from .models import Patient, Assessment
from .forms import PatientForm, AssessmentForm
from django.db.models import Q



@login_required
def patient(request):
    context = {
        'title': 'patient'
    }
    template_name = 'patient/index.html'
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
    template_name = 'patient/create_patient.html'
    return render(request,template_name, context)


@login_required
def patient_list(request):
    patients = Patient.objects.all()
    context = {
        'patients': patients,
        'title': 'Patients',
    }
    template_name = 'patient/patient_list.html'
    return render(request,template_name, context)

@login_required
def add_patient_data(request, pk):
    patient = Patient.objects.get(pk=pk)
    if request.method == 'POST':
        form = AssessmentForm(request.POST)
        if form.is_valid():
            # save the post without commiting to db
            assessment = form.save(commit=False)

            assessment.patient = patient
            assessment.save()

            messages.success(request, f'Patient assessment data added')
            return redirect('patient_detail', patient.id)
    else:
        form = AssessmentForm()
    context = {
        'form': form,
        'patient': patient,
        'title' : 'Assessment',
    }
    template_name = 'patient/add_patient_data.html'
    return render(request,template_name, context)

class PatientDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'patient/patient_detail.html'
    model = Patient
    context_object_name = 'patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Patient Detail'
        return context  
    

@login_required
def health_record(request, pk):
    patient = Patient.objects.get(pk=pk)
    assessments = patient.assessment_set.all()
    context = {
        'assessments': assessments,
        'title' : 'Patient History',
        'patient': patient,
    }
    template_name = 'patient/patient_history.html'
    return render(request,template_name, context)



def search(request):
    if request.method == 'GET':
        query = request.GET.get('q').strip()
        queries = query.split()
        if query is not None:
            if len(queries) == 2:
                lookups = (
                    (Q(first_name__icontains=queries[0]) & Q(last_name__icontains=queries[1])) |
                    (Q(first_name__icontains=queries[1]) & Q(last_name__icontains=queries[0]))
                )
                patients = Patient.objects.filter(lookups).distinct()
            elif len(queries) > 2:
                lookups = (
                    (Q(first_name__icontains=queries[0]) & Q(last_name__icontains=queries[1]) & Q(district__icontains=queries[2])) |
                    (Q(district__icontains=queries[0]) & Q(first_name__icontains=queries[1]) & Q(last_name__icontains=queries[2])) |
                    (Q(first_name__icontains=queries[1]) & Q(last_name__icontains=queries[0]) & Q(district__icontains=queries[2])) |
                    (Q(district__icontains=queries[0]) & Q(first_name__icontains=queries[2]) & Q(last_name__icontains=queries[1]))
                )
                patients = Patient.objects.filter(lookups).distinct()
            else:
                lookups = (
                    Q(first_name__icontains=query) | Q(last_name__icontains=query) |
                    Q(district__icontains=query)
                )
                patients = Patient.objects.filter(lookups).distinct()
            context={
                'patients': patients,
                'search': 'search',
                'title': 'Search Results',
                'query': query,
            }
        else:
            redirect('patients')
    template_name = 'patient/patient_list.html'
    return render(request,template_name, context)
