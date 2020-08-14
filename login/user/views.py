from sqlite3 import IntegrityError, OperationalError

from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate,logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from user.models import Register

username=''
def register(request):

    if request.method == 'POST':  # data sent by user

        email=request.POST['email']
        username = request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        f_name = request.POST['f_name']
        l_name=request.POST['l_name']
        phone=request.POST['phone']

        try:
            obj=Register()
            form =User.objects.create_user(username=username,first_name=f_name,last_name=l_name,email=email,password=password,)
            obj.user=form
            obj.phone=phone
            if password==cpassword:
                obj.save()
            else:
                messages.error(request, 'passwords don\'t match.' )
        except:
            messages.error(request, 'username already taken, try something else.')


    return render(request,"user/signup.html",)


def login(request):

    if request.method=="POST":
        global username
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

        else:
            messages.error(request, 'username or password not correct')
            return redirect('index')

    else:
        return render(request,"user/login.html")

def home(request):

    return render(request,"user/logout.html",)
