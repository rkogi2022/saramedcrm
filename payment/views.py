from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Sum, F
from django.contrib.auth.decorators import login_required

# import models
from prospects.models import business_prospect
from .models import invoice
from .models import receipt
from .models import implementation

# import forms
from .forms import CreateInvoiceForm
from .forms import CreateReceiptForm
from .forms import AddImplementationDetails
#create your views here

# displaying list of invoices
def invoice_details(request):
    invoicedetails=invoice.objects.all().order_by('-created_date')
    page=Paginator(invoicedetails,6)
    page_list=request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'page':page,
        }
    template='payment/invoice.html'
    return render(request,template,context)

# creatin a new invoice
@login_required(login_url='auth_app:login')
def create_invoice(request):
    template='payment/createinvoice.html'
    if request.method == 'POST':
        form=CreateInvoiceForm(request.POST)
        if form.is_valid():            
            form.save()
            messages.success(request, f'The invoice was created successfully')
            return redirect('payment:invoicedetails')
    else:
            form=CreateInvoiceForm()

    return render(request, template,{'form':form})

# delete an invoice
@login_required(login_url='auth_app:login')
def delete_invoice(request,id):
    id = int(id)
    try:
         invoicedetails=invoice.objects.get(id=id)
    except:
        return redirect('payment:invoicedetails')
    invoicedetails.delete()
    return redirect('payment:invoicedetails')

# display receipts
def receipts_details(request):
    paid_amount= receipt.objects.aggregate(total_amount=Sum('amt_paid'))
    receiptsdetails=receipt.objects.all().order_by('-created_date')
    page=Paginator(receiptsdetails,6)
    page_list=request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'page':page,
        'paid_amount':paid_amount,
    }
    template='payment/receipts.html'
    return render(request,template,context)


# creatin a new invoice
@login_required(login_url='auth_app:login')
def addinvoice(request):
    template='payment/createreceipt.html'
    if request.method == 'POST':
        form=CreateReceiptForm(request.POST)
        if form.is_valid():            
            form.save()
            messages.success(request, f'The invoice was created successfully')
            return redirect('payment:receiptsdetails')
    else:
            form=CreateReceiptForm()

    return render(request, template,{'form':form})
@login_required(login_url='auth_app:login')
def update_receipt(request,id):
    receiptdetails=get_object_or_404(receipt, id=id)
    if request.method == 'POST':
        form=CreateReceiptForm(request.POST, instance=receiptdetails)
        if form.is_valid():
            form.save()
            messages.success(request, f'Receipt updated successfully')
            return redirect('payment:receiptsdetails')
    else:
        form=CreateReceiptForm(instance=receiptdetails)
    context={
        'form':form,
        }
    template='payment/updatereceipt.html'
    return render(request,template,context)

#delete a receipt
@login_required(login_url='auth_app:login')
def delete_receipt(request,id):
    id = int(id)
    try:
        receiptdetails=receipt.objects.get(id=id)
    except:
        messages.error(request, f'The receipt was deleted successfully')
        return redirect('payment:receiptsdetails')
    receiptdetails.delete()
    return redirect('payment:receiptsdetails')

# transactional reports view
def transactional_report(request):
    template='payment/transactionalreports.html'

    clients = business_prospect.objects.filter(invoice__isnull=False).distinct()
    report_data = []

    for client in clients:
        invoices = invoice.objects.filter(facilityname=client)
        total_paid = receipt.objects.filter(invoice__in=invoices).aggregate(Sum('amt_paid'))['amt_paid__sum']
        total_paid = total_paid or 0  # If no payments, set total_paid to 0
        total_invoice_amount = invoices.aggregate(Sum('total_cost'))['total_cost__sum']
        balance = total_invoice_amount - total_paid

        report_data.append({
            'client': client,
            'total_invoice_amount': total_invoice_amount,
            'total_paid': total_paid,
            'balance': balance,
        })
    page=Paginator(report_data,10)
    page_list=request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'page':page,
    }
    return render(request,template, context)

# view clients licence expiry
def acc_details(request):
    implementationdetails=implementation.objects.all()
    page=Paginator(implementationdetails,10)
    page_list=request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'page':page,
        }
    template='payment/account.html'
    return render(request, template, context)

# Display implementation dates
def implementation_dates(request, id):
    details=implementation.objects.filter(id=id)
    context={
        'details':details
        }
    template='payment/implementation.html'
    return render(request, template,context )

# add implementation dates
@login_required(login_url='auth_app:login')
def create_implementation(request):
    template='payment/addimplementation.html'
    if request.method == 'POST':
        form=AddImplementationDetails(request.POST,request.FILES)
        if form.is_valid():         
            form.save()
            messages.success(request, f'The dates were added successfully')
            return redirect('payment:clients-details')
    else:
            form=AddImplementationDetails()
    return render(request, template,{'form':form})

@login_required(login_url='auth_app:login')
def update_implementation(request,id):
    implementationdetails=get_object_or_404(implementation, id=id)
    if request.method == 'POST':
        form=AddImplementationDetails(request.POST, instance=implementationdetails)
        if form.is_valid():
            form.save()
            messages.success(request, f'Implementation dates updated successfully')
            return redirect('payment:clients-details')
    else:
        form=AddImplementationDetails(instance=implementationdetails)
    context={
        'form':form,
        }
    template='payment/updateimplementation.html'
    return render(request,template,context)

#delete a receipt
@login_required(login_url='auth_app:login')
def delete_implementation(request,id):
    id = int(id)
    try:
        implementationdetails=implementation.objects.get(id=id)
    except:
        messages.error(request, f'The client details were deleted successfully')
        return redirect('payment:clients-details')
    implementationdetails.delete()
    return redirect('payment:clients-details')