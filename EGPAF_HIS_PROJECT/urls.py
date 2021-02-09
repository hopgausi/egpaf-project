from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('account.urls')),

    path('login/', auth_views.LoginView.as_view(
        template_name='account/login.html',
        redirect_authenticated_user=True), 
        name='login'
        ),

    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', include('dashboard.urls')),
]
