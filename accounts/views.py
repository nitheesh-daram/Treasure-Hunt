from accounts.decorators import unauthenticated_user
from django.shortcuts import render, redirect
from .forms import RegisterForm,login
from django.contrib import messages
# Create your views here.
from django.contrib.auth import authenticate,login,logout

def register(request):
    if not request.user.is_authenticated:
        if request.POST:
            form = RegisterForm(request.POST)
            if form.is_valid():
                if  form.email_check():
                    messages.info(request,"Email Already exists")
                    return redirect('register')
                form.save()
                user=form.cleaned_data.get("username")
                messages.success(request,"Account was created for "+ user)
                return redirect('login')
        else:
            form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})
    else:
        return redirect("Home_Page")

def loginuser(request):
    if request.user.is_authenticated:
        return redirect("Home_Page")
    else:
        if request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('Home_Page')
            else:
                messages.info(request,"Username or Password is incorrect")
                return redirect("login")
        return render(request,"accounts/login.html",{})

