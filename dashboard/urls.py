from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('create_patient/', views.create_patient, name="create_patient"),
    path('patients/', views.patient_list, name="patients"),
]