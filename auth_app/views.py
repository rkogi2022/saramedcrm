# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# import mesagess
from django.contrib import messages
# import forms
from .forms import CreateUserForm

# import models
from calls.models import support 
from payment.models import implementation
# Create your views here.

# register a new user
def registerpage(request):
    if request.user.is_authenticated:
        return redirect()
    else:
        form=CreateUserForm()
        
        if request.method == 'POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('auth_app:login')

        context={'form':form}
        return render(request, 'auth_app/register.html',context)

# login
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('auth_app:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user =authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect ('auth_app:home')
            else:
                messages.info(request, 'Username OR Password is Incorrect')
                
        context={}
        return render(request,'auth_app/login.html',context)

# logout
def logoutUser(request):
    logout(request)
    return redirect('auth_app:login')


# index page
def index(request):
    totaldata=implementation.objects.all().count()

    pendingcount = support.objects.filter(status__contains='PENDING').count()
    donecount = support.objects.filter(status__contains='DONE').count()

    registercount = support.objects.filter(module__contains='PATIENT REGISTER').count()
    nursecount = support.objects.filter(module__contains='NURSE').count()
    doctorcount = support.objects.filter(module__contains='DOCTOR').count()
    labcount = support.objects.filter(module__contains='LABORATORY').count()
    radiographycount = support.objects.filter(module__contains='RADIOGRAPHY').count()
    inpatientcount = support.objects.filter(module__contains='INPATIENT').count()
    pharmacycount = support.objects.filter(module__contains='PHARMACY').count()
    cashiercount = support.objects.filter(module__contains='CASHIER').count()
    inventorycount = support.objects.filter(module__contains='INVENTORY').count()
    financecount = support.objects.filter(module__contains='FINANCE').count()
    humancount = support.objects.filter(module__contains='HUMAN RESOURCE').count()
    systemcount = support.objects.filter(module__contains='SYSTEM ADMIN').count()
    

    context={
        'totaldata':totaldata,

        'pendingcount':pendingcount,
        'donecount':donecount,

        'registercount':registercount,
        'nursecount':nursecount,
        'doctorcount':doctorcount,
        'labcount':labcount,
        'radiographycount':radiographycount,
        'inpatientcount':inpatientcount,
        'pharmacycount':pharmacycount,
        'cashiercount':cashiercount,
        'inventorycount':inventorycount,
        'financecount':financecount,
        'humancount':humancount,
        'systemcount':systemcount
    }
    template='index.html'
    return render(request, template,context)