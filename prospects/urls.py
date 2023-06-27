from django.urls import path
from  . import views

app_name='prospects'

urlpatterns = [
    # business prospects
    path('view_business_prospects/', views.view_business_prospects, name='business-prospects'),
    path('<int:prospect_id>/feedback/', views.save_feedback, name='save_feedback'),
    path('create_business_prospect/',views.create_business_prospect, name='create-prospect'),
    path('update_business_prospect/<int:lead_id>/', views.update_business_prospect, name='update-prospects'),

    # conversion tracker
    path('view_conversion_progress/', views.view_conversion_progress, name='conversion-tracker'),
    path('add_conversion_details',views.add_conversion_details,name='add-conversion-details'),
    path('demo_details/<int:id>/', views.demo_details,name='demo-details'),
    path('update_demo_details/<int:pk>',views.update_demo_details, name='update_demo_details'),   

]