from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    
    path('', views.loginPage,name='login1'),
    path('index', views.index,name='home'),
    path('team', views.team,name='team'),
    path('design', views.design,name='design'),
    #path('login_in', views.login_in,name='login_in'),
    path('register/',views.registerPage,name='register'),
    path('login1/',views.loginPage,name='login1'),
    path('logout/',views.logoutUser,name='logout')

]