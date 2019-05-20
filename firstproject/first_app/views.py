from django.shortcuts import render
from first_app import forms


# Create your views here.
from django.http import HttpResponse
from first_app.models import AccessRecord,Webpage,Topic

def index(request):
    web_pagelist = AccessRecord.object.order_by('date')
    webpage_display=Webpage.object.order_by('url')
    my_dict={'insert_me':web_pagelist,'testing':webpage_display} 
    return render(request,'first_app/index.html',context=my_dict)
def testing(request):
    return HttpResponse("hello srikanth :)")
def justtry(request):
    return render(request,'second_app/help.html',context=None)
def form_name_view(request):
     form=forms.FormName()
     
     if request.method =='POST':

         form = forms.FormName(request.POST)

         if form.is_valid():
             print("form is valid")
             print('NAME:'+form.cleaned_data['name'])
             print('EMAIL:'+form.cleaned_data['email'])
             print('TEXT:'+form.cleaned_data['text'])


     return render(request,'first_app/formtest.html',{'form':form})      

