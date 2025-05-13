from django.shortcuts import render,redirect,HttpResponse
from .models import * 
from .forms import *

# Create your views here.
def blogdata(request):
    blog_data=Blog.objects.all()
    context={'blog_data':blog_data}
    return render(request,'bloglist.html',context)

def createblog(request):
    
    fm=PostModelForm()
    if request.method=="POST":
        fm=PostModelForm(request.POST,request.FILES)
        if fm.is_valid():
            print(fm)
            fm.save()
          
            return redirect('/blog')
        else:
           
            return HttpResponse('Error')
    return render(request,'create.html',{'fm':fm})