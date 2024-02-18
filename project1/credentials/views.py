from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()
                print("user created")
                return redirect('login')

        else:
            messages.info(request, "Password not matching")
            return redirect('register')
            # print("Password not matching")
        return redirect('/')
    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    # else:
    #     print("something went wrong")

    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

def result(request):
    return render(request, "result.html")

def form(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        DOB = request.POST['DOB']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']

        user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, DOB=DOB, age=age, gender=gender, phone=phone,  email=email, address=address)
        user.save()
        return redirect(request, 'result')
    return render(request, "form.html")
