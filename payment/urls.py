from django.urls import path
from  . import views

app_name='payment'

urlpatterns = [
    # invoice model 
    path('invoice_details/', views.invoice_details, name='invoicedetails'),
    path('create_invoice/', views.create_invoice, name='createinvoice'),
    path('delete_invoice/<int:id>/',views.delete_invoice, name='delete_invoice'),

    # receipts model
    path('receipts_details/', views.receipts_details, name='receiptsdetails'),
    path('addinvoice/', views.addinvoice, name='addinvoice'),
    # path('create_receipt/',views.create_receipt, name='createreceipt'),
    path('update_receipt/<int:id>',views.update_receipt, name='update_receipt'),
    path('delete_receipt/<int:id>',views.delete_receipt, name='delete_receipt'),

        # implementation details 
    path('acc_details', views.acc_details, name='clients-details'),
    path('implementation_dates/<int:id>/', views.implementation_dates, name='implementation_dates'),
    path('create_implementation',views.create_implementation, name='create_implementation'),
    path('update_implementation/<int:id>',views.update_implementation, name='update_implementation'),
    path('delete_implementation/<int:id>/',views.delete_implementation, name='delete_implementation'),

        # transactional reports
    path('transactional_report/', views.transactional_report, name='transactional_report'),
]
