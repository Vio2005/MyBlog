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

def blogdetail(request,id):
    data=Blog.objects.filter(id=id)
    
    context={"data":data}
    return render(request,'blogdetail.html',context)

def blogdelete(request,id):
    data=Blog.objects.filter(id=id).delete()
    return redirect('/blog')


def updateblog(request, id):
    data = Blog.objects.get(id=id)
    obj = PostModelForm(request.POST, request.FILES, instance=data)
    if obj.is_valid():
        obj.save()
    return redirect('/blog')




