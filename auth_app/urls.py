from django.urls import path
from  . import views

app_name='auth_app'

urlpatterns = [
    path('register/',views.registerpage,name='register'),
    path('', views.loginpage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('index', views.index, name='home')
]