from django.shortcuts import render,redirect
from home.models import Logins
from django.contrib import messages
#from .models import Logins
#from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
# Create your views here.
def index(request):
    return render(request,'index.html')
    
def team(request):
    return render(request,"team.html")

def design(request):
    event_list= Logins.objects.all()
    return render(request,"design.html",{'event_list':event_list})

def login(request):
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
    context ={}
    return render(request,'login1.html',context)

