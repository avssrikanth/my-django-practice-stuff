"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from first_app import views
from second_app import views as v 
from third_app import views as v2

urlpatterns = [
    path('first',include('first_app.urls')), 
    path('help',v.help),
   
    path('second',v.srikanth),
    path('admin/', admin.site.urls),
    path('helppage/',views.justtry),
    path('form',views.form_name_view,name="formpage"),
    path('signup',v.form),
    path('',v2.index,name='index'),
    path('logout',v2.user_logout,name='logout'),
    path('third_app',include('third_app.urls')),
    path('login',v2.user_login,name="login"),
]
 