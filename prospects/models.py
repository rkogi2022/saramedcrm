from django.db import models
from django.conf import settings


# Create your models here.
class business_prospect(models.Model):
    lead_id=models.AutoField(primary_key=True)
    facility_name=models.CharField(max_length=300)
    county=models.CharField(max_length=30)
    town=models.CharField(max_length=30)
    email=models.EmailField(blank=True, null=True)
    contact_person=models.CharField(max_length=200, null=True, blank=True)
    phone_no=models.CharField(max_length=20, null=True, blank=True)
    comment=models.TextField(blank=True)
    created_date=models.DateField(auto_now_add=False, auto_now= False)

    def __str__(self):
        return self.facility_name
    
class Feedback(models.Model):
    prospect = models.ForeignKey(business_prospect, on_delete=models.CASCADE)
    feedback = models.TextField(blank=True)
    feedback_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.prospect,self.feedback
    
class conversion_tracker(models.Model):

    meeting=[
        ('PHYSICAL', 'PHYSICAL'),
        ('VIRTUAL', 'VIRTUAL'),
    ]
    status=[
        ('DONE', 'DONE'),
        ('PENDING', 'PENDING'),
    ]
    demo_id=models.ForeignKey(business_prospect,null=True, on_delete=models.CASCADE)
    demostatus=models.CharField(max_length=30,choices=status,default='PENDING')
    demodate=models.DateField(null=True, blank=True, default=None)
    Attendees=models.TextField(blank=True)
    meeting=models.CharField(max_length=30,choices=meeting,blank=True)
    feedback=models.TextField(blank=True)
    assessmentdate=models.DateField(null=True, blank=True, default=None)
    report=models.FileField(upload_to='documents/' ,blank=True)
    reportdate=models.DateField(null=True, blank=True, default=None)
    expression=models.FileField(upload_to='documents/' ,blank=True)
    facility_license=models.FileField(upload_to='documents/' ,blank=True)
    krapin=models.FileField(upload_to='documents/' ,blank=True)
    created_by=models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.demo_id}'