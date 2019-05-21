from django.shortcuts import render
from django.http import HttpRequest
from third_app.forms import Userform,UserProfileInfoForm
from third_app.models import User,UserProfileInfo
# Create your views here.

from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect,HttpRequest,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

 
def index(request):
    return render(request,'third_app/index.html',context=None)
def register(request):
    registered=False

    if request.method=="POST":
        user_form=Userform(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user #for one to one relationship 
            if 'profile_pics'in request.FILES:
                profile.profile_pics=request.FILES['profile_pics']
            profile.save()

            registered=True
        else:
            print(user_form.errors,profile_form.errors)          

    else:
        user_form=Userform()
        profile_form=UserProfileInfoForm()

    return render(request,'third_app/registration.html',context={'user_form':user_form,'profile_form':profile_form,'registered':registered})     

def user_login(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:

                login(request,user)
                return HttpResponseRedirect(reverse('index'))
                
            else:
                 return HttpResponse("Account not active")
        else:
            return HttpResponse("invalid login detils")

    else:
        return render(request,'third_app/login.html',{}) 


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("hey you are loged in")    