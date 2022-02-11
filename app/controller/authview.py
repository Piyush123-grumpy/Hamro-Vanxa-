from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib import messages
from account.models import Account

from app.forms import CustomUserForm

def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registered Successfully! Login to Continue")
            return redirect('/login')
    context = {'form':form}
    return render(request,"app/customerregistration.html",context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,"You are already logged in")
        return redirect('/')

    else:
        if request.method =='POST':
            name = request.POST.get('username')
            print(name)
            passwd = request.POST.get('password')
            print(passwd)

            user = authenticate(request, username=name, password=passwd)
            
            if user is not None:
                login(request, user)
                messages.success(request,"Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request, "Invalid Username or Password")
                print("Okay")
                return redirect("/login")
        return render(request,"app/login.html")

def logoutpage(request):
    if request.user.is_authenticated:
        messages.success(request,"Logged out successfully")
        logout(request)
    return redirect("/")
