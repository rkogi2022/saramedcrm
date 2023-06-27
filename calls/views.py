from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import support
from .forms import AddSupportCallForm
from .forms import UpdateSupportCallForm

from .models import courtesy
from .forms import AddCourtesyCallForm
from .models import director
from .forms import AddDirectorCallForm

# Create your views here.
# display all logged support calls
def viewsupportcall(request):
        supportdetails=support.objects.all().order_by('-logdate')
        page=Paginator(supportdetails,10)
        page_list=request.GET.get('page')
        page = page.get_page(page_list)
        context={
            'page':page,
            }
        template='calls/support.html'
        return render(request, template, context)

# add support call
@login_required(login_url='auth_app:login')
def addsupportcall(request):
    template='calls/addsupportcalldetails.html'
    if request.method == 'POST':
        form=AddSupportCallForm(request.POST)
        if form.is_valid():            
            form.save()
            messages.success(request, f'The call was logged successfully')
            return redirect('calls:viewsupportcall')
    else:
            form=AddSupportCallForm()
    return render(request, template,{'form':form})

# update supportcall
@login_required(login_url='auth_app:login')
def update_supportcall(request,id):
    supportdetails=get_object_or_404(support, id=id)
    if request.method == 'POST':
        form=UpdateSupportCallForm(request.POST, instance=supportdetails)
        if form.is_valid():
            form.save()
            messages.success(request, f'Support call details updated successfully')
            return redirect('calls:viewsupportcall')
    else:
        form=UpdateSupportCallForm(instance=supportdetails)
    context={
        'form':form,
        }
    template='calls/updatesupportcall.html'
    return render(request,template,context)

#delete a support call
@login_required(login_url='auth_app:login')
def delete_supportcall(request,id):
    id = int(id)
    try:
        calldetails=support.objects.get(id=id)
    except:
        messages.error(request, f'The call details were deleted successfully')
        return redirect('calls:viewsupportcall')
    calldetails.delete()
    return redirect('calls:viewsupportcall')    

# search by module or status
@login_required(login_url='users:login')
def supportcall_searchbar(request):
    if request.method == 'GET':
        searched=request.GET.get('searched')
        if searched:
            multiple_searched=Q(Q(module__contains=searched) |Q(status__contains=searched))
            searcheddetails=support.objects.filter(multiple_searched)
            return render(request, 'calls/search.html',{'searcheddetails':searcheddetails})
        else:
            return render(request, 'calls/search.html',{})

# view the call details ie problem and sol offered
def viewcalldetails(request, id):
    calldetails=support.objects.filter(id=id)
    context={
        'calldetails':calldetails
        }
    template='calls/supportdetails.html'
    return render(request, template,context )

# update the call details
@login_required(login_url='auth_app:login')
def update_calldetails(request,id):
    supportdetails=get_object_or_404(support, id=id)
    if request.method == 'POST':
        form=AddSupportCallForm(request.POST, instance=supportdetails)
        if form.is_valid():
            form.save()
            messages.success(request, f'Support call details updated successfully')
            return redirect('calls:viewsupportcall')
    else:
        form=AddSupportCallForm(instance=supportdetails)
    context={
        'form':form,
        }
    template='calls/updatesupportcall.html'
    return render(request,template,context)


# view courtesy calls
def viewcourtesycall(request):
        courtesydetails=courtesy.objects.all().order_by('-logdate')
        page=Paginator(courtesydetails,10)
        page_list=request.GET.get('page')
        page = page.get_page(page_list)
        context={
            'page':page,
            }
        template='calls/courtesy.html'
        return render(request, template, context)

# add courtesy calls
@login_required(login_url='auth_app:login')
def addcourtesycall(request):
    template='calls/addcourtesy.html'
    if request.method == 'POST':
        form=AddCourtesyCallForm(request.POST)
        if form.is_valid():            
            form.save()
            messages.success(request, f'The call was logged successfully')
            return redirect('calls:viewcourtesycall')
    else:
            form=AddCourtesyCallForm()
    return render(request, template,{'form':form})

# update courtesy calls
@login_required(login_url='auth_app:login')
def update_courtesycall(request,id):
    courtesydetails=get_object_or_404(courtesy, id=id)
    if request.method == 'POST':
        form=AddCourtesyCallForm(request.POST, instance=courtesydetails)
        if form.is_valid():
            form.save()
            messages.success(request, f'Courtesy call details updated successfully')
            return redirect('calls:viewcourtesycall')
    else:
        form=AddCourtesyCallForm(instance=courtesydetails)
    context={
        'form':form,
        }
    template='calls/updatecourtesy.html'
    return render(request,template,context)

# deleting courtesy call
@login_required(login_url='auth_app:login')
def delete_courtesycall(request,id):
    id = int(id)
    try:
        calldetails=courtesy.objects.get(id=id)
    except:
        messages.error(request, f'The call details were deleted successfully')
        return redirect('calls:viewcourtesycall')
    calldetails.delete()
    return redirect('calls:viewcourtesycall')    

# view directors' calls
def viewdirectorscall(request):
        directorsdetails=director.objects.all().order_by('-logdate')
        page=Paginator(directorsdetails,10)
        page_list=request.GET.get('page')
        page = page.get_page(page_list)
        context={
            'page':page,
            }
        template='calls/director.html'
        return render(request, template, context)

# add directors calls
@login_required(login_url='auth_app:login')
def adddirectorscall(request):
    template='calls/adddirectorscall.html'
    if request.method == 'POST':
        form=AddDirectorCallForm(request.POST)
        if form.is_valid():            
            form.save()
            messages.success(request, f'The call was logged successfully successfully')
            return redirect('calls:viewdirectorscall')
    else:
            form=AddDirectorCallForm()
    return render(request, template,{'form':form})

# update directors calls
@login_required(login_url='auth_app:login')
def update_directorscall(request,id):
    directorsdetails=get_object_or_404(director, id=id)
    if request.method == 'POST':
        form=AddDirectorCallForm(request.POST, instance=directorsdetails)
        if form.is_valid():
            form.save()
            messages.success(request, f'Courtesy call details updated successfully')
            return redirect('calls:viewdirectorscall')
    else:
        form=AddDirectorCallForm(instance=directorsdetails)
    context={
        'form':form,
        }
    template='calls/updatedirectors.html'
    return render(request,template,context)

# deleting directors call
@login_required(login_url='auth_app:login')
def delete_directorscall(request,id):
    id = int(id)
    try:
        calldetails=director.objects.get(id=id)
    except:
        messages.error(request, f'The call details were deleted successfully')
        return redirect('calls:viewdirectorscall')
    calldetails.delete()
    return redirect('calls:viewdirectorscall')    
