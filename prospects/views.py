from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.utils import timezone

# import mesagess
from django.contrib import messages

# import models
from .models import business_prospect
from .models import Feedback
from .models import conversion_tracker

# import forms
from .forms import AddBussinessProspectForm
from .forms import FeedbackForm
from .forms import ConversionTrackerForm

# Create your views here.

# display the business prospect details
def view_business_prospects(request):
    prospects=business_prospect.objects.all().order_by('-created_date')
    page=Paginator(prospects,10)
    page_list=request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'page':page,
        }
    template='prospects/businessprospects.html'
    return render(request, template, context)

# show the comments and feedback given and also add a new feedback
def save_feedback(request, prospect_id):
    prospect = get_object_or_404(business_prospect, pk=prospect_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.cleaned_data['feedback']
            Feedback.objects.create(prospect=prospect, feedback=feedback)
            return redirect('prospects:save_feedback',prospect_id)
    else:
        form = FeedbackForm()
        return render(request, 'prospects/feedback.html', {'prospect': prospect, 'form': form})

# adding a new business prospect
@login_required(login_url='auth_app:login')
def create_business_prospect(request):
    template='prospects/createprospect.html'
    if request.method == 'POST':
        form=AddBussinessProspectForm(request.POST)
        if form.is_valid():            
            form.save()
            messages.success(request, f'Prospect added successfully')
            return redirect('prospects:business-prospects')
    else:
            form=AddBussinessProspectForm()

    return render(request, template,{'form':form})
     
# update business prospects details
@login_required(login_url='auth_app:login')
def update_business_prospect(request, lead_id):
    template='prospects/updatebusinessprospect.html'
    prospects = get_object_or_404(business_prospect, pk=lead_id)
    if request.method == 'POST':
         form=AddBussinessProspectForm(request.POST, instance=prospects)
         if form.is_valid():
              form.save()
              messages.success(request, f'Details updated successfully')
              return redirect('prospects:business-prospects')
    else:
        form=AddBussinessProspectForm(instance=prospects)
    return render(request,template,{'form':form})

# view the conversion progress details
def view_conversion_progress(request):
    progress=conversion_tracker.objects.all().order_by('-demo_id')
    page=Paginator(progress,10)
    page_list=request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'page':page,
        }
    template='prospects/conversionprogress.html'
    return render(request, template, context)

# adding conversion progress details ie demo details, site assesment details and supporting doc
@login_required(login_url='auth_app:login')
def add_conversion_details(request):
    template='prospects/addconversionprogress.html'
    if request.method == 'POST':
        form=ConversionTrackerForm(request.POST,request.FILES)
        if form.is_valid():            
            form.save()
            messages.success(request, f'Conversion details added successfully')
            return redirect('prospects:conversion-tracker')
    else:
            form=ConversionTrackerForm()

    return render(request, template,{'form':form})


# view the demo details per client
def demo_details(request,id):
    demo=conversion_tracker.objects.filter(id=id)
    context={
        'demo':demo
        }
    template='prospects/demodetails.html'
    return render(request, template, context)


# update the conversion details of a client
@login_required(login_url='auth_app:login')
def update_demo_details(request, pk):
    demodetails=conversion_tracker.objects.get(id=pk)
    if request.method == 'POST':
        form=ConversionTrackerForm(request.POST, instance=demodetails)
        if form.is_valid():
            form.save()
            messages.success(request, f'Details sucessfully updated for  {pk}')
            return redirect('prospects:demo-details',pk)
    else:
        form=ConversionTrackerForm(instance=demodetails)
    context={
        'form':form,
        }

    return render(request,'prospects/demodetailsupdate.html',context)
