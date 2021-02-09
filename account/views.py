from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib import messages

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created, Login!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
        'title':'Register',
    }
    template_name = 'account/register.html'
    return render(request, template_name, context)


@login_required
def user_list(request):
    users = User.objects.all()
    context = {
        'users': users,
        'title': 'Users',
    }
    template_name = 'account/users_list.html'
    return render(request,template_name, context)