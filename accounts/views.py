from django.shortcuts import render, redirect
from .models import Account
from .forms import AccountRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages




def RegisterUser(request):
    
    form = AccountRegisterForm()
    if request.method == 'POST':
        form = AccountRegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user( first_name = first_name, last_name = last_name, email = email, username = username, password = password)
            user.save()

            return redirect('LoginUser')

    context = {
        'form' : form
    }
    return render(request, 'auth/register.html', context)



def LoginUser(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)              
            return redirect('UserPage')
        else:
            messages.info(request, 'Username or Password is incorrect')

    
    return render(request, 'auth/login.html')


def UserPage(request):
    return render(request, 'auth/user.html')

def UserLogout(request):
    logout(request)
    return redirect('LoginUser')

