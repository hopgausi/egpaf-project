from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name="register"),
    path('users/', views.user_list, name="users"),
]