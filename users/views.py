from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from users.models import CustomUser
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('./profile')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('./login')
    else:
        return render(request, 'login.html')

def register(request):

    if request.method == 'POST':
        name = request.POST['name']
        sex = request.POST['sex']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        password2 = request.POST['password2']
        image = request.FILES['image']
        address = request.POST['address']

        if password == password2:
            if CustomUser.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken!')
                return redirect('register')
            elif CustomUser.objects.filter(mobile=mobile).exists():
                messages.info(request, 'Mobile Already Taken!')
                return redirect('register')
            else:
                user = CustomUser(name=name, sex=sex, username=email, email=email, mobile=mobile, password=password, image=image, address=address)
                user.set_password(password)
                user.save()
                print('user created')
                return redirect('./login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')
    
def logout(request):
    auth.logout(request)
    return redirect('./login')

@login_required(login_url='users:login')
def profile(request):
    return render(request, 'profile.html')