from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login as auth_login
from profileapp.models import Profile
# Create your views here.

def signup(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST['name']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists!')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username is already taken!')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=name, last_name=lastname)
                user.save()

                new_profile = Profile.objects.create(username=user, name=name, last_name=lastname)
                new_profile.save()
                return redirect('login')
        else:
            messages.info(request, 'passwords do not match')
            return redirect('signup')
    else:

        return render(request, 'registrationapp/registration.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/success')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'registrationapp/login.html')

def success(request):
    return render(request, 'registrationapp/success.html')