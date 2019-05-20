from django.urls import path
from first_app import views
app_name='first_app'
urlpatterns = [
    path('',views.index),
    path('/testing',views.testing,name='testing' ) ,

    
]
