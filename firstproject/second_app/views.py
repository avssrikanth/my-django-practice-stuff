from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpRequest
from second_app.models import MyUser
from second_app.forms import Newuserform
def srikanth(request):
    userrec=MyUser.object.order_by('first_name')
    myvar={"insert_me_fromsecond_app":"hey srikanth i am from second application:)","userrecords":userrec}
    return render(request,'second_app/second_index.html',context=myvar)
def help(request):
    dic={"uname":"srikanth",'t':'Have a good day:)'}
    return render(request,"second_app/help.html",context=dic)    

def form(request):
    form = Newuserform()

    if request.method == "POST":
      form =Newuserform(request.POST)

      if form.is_valid():
          form.save(commit=True)
      
          return srikanth(request)
      else:
         return HttpResponse("error")

    return render(request,'second_app/signup.html',{"form":form})  