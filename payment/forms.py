from django import forms

# import your models
from . models import invoice
from . models import receipt
from .models import implementation

#custom date widget
class DateInput(forms.DateInput):
    input_type = 'date'

class CreateInvoiceForm(forms.ModelForm):
    class Meta:
 
        model=invoice
        fields=('facilityname','project_cost',)
        widgets = {
            'facilityname': forms.Select(attrs={'class': 'form-control'}),
            'project_cost': forms.TextInput(attrs={'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


class CreateReceiptForm(forms.ModelForm):
    transaction_date=forms.DateTimeField(label='Transaction Date',widget=DateInput(attrs={'class':'form-control'}),required=True)
    class Meta:
        model=receipt
        fields=('__all__')
        exclude = ['created_by','created_date']  

        widgets = {
            'facilityname': forms.Select(attrs={'class': 'form-control'}),
            'invoice': forms.Select(attrs={'class': 'form-control'}),
            'payment_mode': forms.Select(attrs={'class': 'form-control'}),
            'amt_paid': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_mode': forms.Select(attrs={'class': 'form-control'}),
        }
        def __init__(self, *args, **kwargs):
             super().__init__(*args, **kwargs)


class AddImplementationDetails(forms.ModelForm):
    start_date=forms.DateTimeField(label='Start Date',widget=DateInput(attrs={'class':'form-control'}),required=True)
    golive_date=forms.DateField(label='Go-Live Date',widget=DateInput(attrs={'class':'form-control'}),required=True)
    end_date=forms.DateField(label='End Date',widget=DateInput(attrs={'class':'form-control'}),required=True)
    class Meta:
        model=implementation
        fields=('facility_name','start_date','golive_date','end_date','implementation_report')
        widgets = {
            'facility_name': forms.Select(attrs={'class': 'form-control'}),
            'implementation_report': forms.FileInput(attrs={'class': 'form-control'}),
        }
        def __init__(self, *args, **kwargs):
             super().__init__(*args, **kwargs)
