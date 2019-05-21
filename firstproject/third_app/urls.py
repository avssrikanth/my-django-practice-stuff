from django import urls
from django.urls import path
from third_app import views
app_name='third_app'

urlpatterns = [

    path('register',views.register,name='register'),
   
   

]
