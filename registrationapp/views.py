from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from profileapp.models import Profile
# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists!')
                return redirect('signup/')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username is already taken!')
                return redirect('signup/')
            else:
                user = User.objects.create_user(firstname=firstname, lastname=lastname, username=username, email=email, password=password1)
                user.save()

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('login/')
        else:
            messages.info(request, 'passwords do not match')
            return redirect('signup/')
    else:

        return render(request, 'registrationapp/registration.html')
    
def login(request):
    return render(request, 'registrationapp/login.html')