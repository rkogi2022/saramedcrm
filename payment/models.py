from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from datetime import date,timedelta
from django.db.models import Sum
from prospects.models import business_prospect
from django.conf import settings

# Create your models here.

# Create your models here.
# model to track initial invoice billed
class invoice(models.Model):
    facilityname=models.ForeignKey(business_prospect,null=True, on_delete=models.CASCADE)
    project_cost=models.IntegerField(default=0, null=False, blank=False)
    tax=models.IntegerField(default=0)
    total_cost=models.IntegerField(default=0,unique=False)
    created_date = models.DateTimeField(default=timezone.now)
    created_by=models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

# function to calculate the tax and total amount
    def save(self, *args, **kwargs):
        Value_Added_Tax=0.16
        self.tax=(int(self.project_cost)) * Value_Added_Tax
        self.total_cost=(int(self.tax) + int(self.project_cost))
        return super().save(*args, **kwargs)

    
    def __str__(self):
        return f"{self.facilityname}-{self.project_cost}"
    

class receipt(models.Model):
    mode=[
        ('MPESA ', 'Mpesa'),
        ('CHEQUE', 'Cheque'),
        ('BANK-TRANSACTION','Bank Payment'),
    ]

    facilityname=models.ForeignKey(business_prospect,null=True, on_delete=models.CASCADE)
    invoice = models.ForeignKey(invoice, on_delete=models.CASCADE)
    amt_paid=models.PositiveIntegerField(default=0)
    payment_mode=models.CharField(max_length=20,choices=mode, default='Mpesa')
    transaction_date = models.DateField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)
    created_by=models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return f'{self.facilityname}'



class implementation(models.Model):
    id=models.BigAutoField(primary_key=True)
    facility_name=models.ForeignKey(receipt, null=True, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    golive_date=models.DateField(null=True, blank=True)
    end_date= models.DateField(null=True, blank=True)
    no_of_days=models.CharField(max_length=20,blank=True)
    license_due=models.DateField(default=timezone.now)
    implementation_report=models.FileField(upload_to='documents/' ,blank=True)

    def save(self, *args, **kwargs):
        self.license_due=self.golive_date + timedelta(days=366)

        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.facility_name}'