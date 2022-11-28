from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    
    path('', views.index,name='home'),
    path('team', views.team,name='team'),
    path('design', views.design,name='design'),
    #path('login', views.login,name='login'),
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login')

]