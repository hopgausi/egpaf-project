from django.urls import path
from . import views


urlpatterns = [
    path('', views.patient, name="patient"),
    path('create-patient/', views.create_patient, name="create_patient"),
    path('patients/', views.patient_list, name="patients"),
    path('add-patient-data/patient/<int:pk>/', views.add_patient_data, name="add_patient_data"),
    path('patient/<int:pk>/', views.PatientDetailView.as_view(), name='patient_detail'),
    path('patient/<int:pk>/health-record', views.health_record, name="health_record"),
    path('search/', views.search, name="search"),
]