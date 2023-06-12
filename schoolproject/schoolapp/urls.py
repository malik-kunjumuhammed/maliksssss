from . import views
from django.urls import path
app_name='schoolapp'

urlpatterns = [

    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register', views.register, name='register'),
    path('button',views.button,name='button'),
    path('form',views.form,name='form'),

]