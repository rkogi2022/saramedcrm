
from django import forms
from . models import support
from .models import courtesy
from .models import director


#custom date widget
class DateInput(forms.DateInput):
    input_type = 'date'

class AddSupportCallForm(forms.ModelForm):
    logdate=forms.DateTimeField(label='Log Date',widget=DateInput)
    completiondate=forms.DateTimeField(label='Completion Date',widget=DateInput,required=False)
    problem=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),required=True)
    solution=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),required=False)
    class Meta:
        model=support
        fields=('__all__')
        widgets = {
            'facility': forms.Select(attrs={'class': 'form-control'}),
            'status':forms.Select(attrs={'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)



class UpdateSupportCallForm(forms.ModelForm):
    logdate=forms.DateTimeField(label='Date',widget=DateInput)
    problem=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),required=True)
    solution=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),required=False)
    completiondate=forms.DateTimeField(label='Completion Date',widget=DateInput,required=False)
    class Meta:
        model=support
        fields=('facility','logdate','module','problem','status')
        widgets = {
            'facility': forms.Select(attrs={'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class AddCourtesyCallForm(forms.ModelForm):
    logdate=forms.DateTimeField(label='Date',widget=DateInput(attrs={'class':'form-control'}),required=True)
    feedback=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),required=True)
    class Meta:
        model=courtesy
        fields=('__all__')
        widgets = {
            'facility': forms.Select(attrs={'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class AddDirectorCallForm(forms.ModelForm):
    feedback_given=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),required=True)
    logdate=forms.DateTimeField(label='Date',widget=DateInput(attrs={'class':'form-control'}),required=True)
    class Meta:
        model=director
        fields=('__all__')

        widgets = {
            'facility_name': forms.Select(attrs={'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)