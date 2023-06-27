from django.urls import path
from  . import views

app_name='calls'

urlpatterns = [
    # support model urls 
    # support call logs urls
    path('viewsupportcall/',views.viewsupportcall, name='viewsupportcall'),
    path('addsupportcall/', views.addsupportcall, name='addsupportcall'),
    path('update_supportcall/<int:id>/', views.update_supportcall, name='update_supportcall'),
    path('delete_supportcall/<int:id>/', views.delete_supportcall, name='delete_supportcall'),
    path('supportcall_searchbar/',views.supportcall_searchbar, name='supportcall_searchbar'),
    # update the call details ie sol offered
    path('viewcalldetails/<int:id>/',views.viewcalldetails, name='viewcalldetails'),
    path('update_calldetails/<int:id>/',views.update_calldetails, name='update_calldetails'),

    # courtesy model urls
    path('viewcourtesycall/', views.viewcourtesycall, name='viewcourtesycall'),
    path('addcourtesycall/', views.addcourtesycall, name='addcourtesycall'),
    path('update_courtesycall/<int:id>/',views.update_courtesycall, name='update_courtesycall'),
    path('delete_courtesycall/<int:id>/',views.delete_courtesycall, name='delete_courtesycall'),

    # directors model
    path('viewdirectorscall/',views.viewdirectorscall, name='viewdirectorscall'),
    path('adddirectorscall/', views.adddirectorscall, name='adddirectorscall'),
    path('update_directorscall/<int:id>/', views.update_directorscall, name='update_directorscall'),
    path('delete_directorscall/<int:id>/', views.delete_directorscall, name='delete_directorscall'),
]
