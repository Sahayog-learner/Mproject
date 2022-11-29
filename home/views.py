from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout

from home.models import Logins
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')
    
def team(request):
    return render(request,"team.html")

def design(request):
    event_list= Logins.objects.all()
    return render(request,"design.html",{'event_list':event_list})

def login_in(request):
    if request.method=="POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        login=Logins(name=name,email=email,phone=phone)
        login.save()
        messages.success(request, 'Successfully sent!!.')
    return render(request,"login.html")

def registerPage(request):
    form= CreateUserForm ( )

    if request.method == "POST":
        form= CreateUserForm(request.POST )
        if form.is_valid():
             form.save()
             user= form.cleaned_data.get("username") # for retreiving the username from form registration
             messages.success(request, 'Account was created for '+ user)
             return redirect('login1')

    context ={'form':form}
    return render(request,'register.html',context)

def loginPage(request):

    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else :
            messages.info(request,"Username OR Password is incorrect")
            

    context ={}
    return render(request,'login1.html',context)
    
def logoutUser(request):
    logout(request)
    return redirect('login1')


