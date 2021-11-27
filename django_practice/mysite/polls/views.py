from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import InfoForm,UpForm,DelForm
from .models import Info

def home(request):
    return render(request,'polls/home.html')
    
def insert(request, uid=1):
    if request.method=='POST':
        inform=InfoForm(request.POST)
        if inform.is_valid():
            inform.save()
            messages.info(request,'Information stored Successfully')
            return redirect(insert)
        else:
            messages.info(request,'Invalid data')
            return redirect(insert)    
    else:
        inform=InfoForm()
        return render(request,'polls/insert.html',{'inform':inform})    

def display(request):
   data=Info.obj.all() 
   return render(request,'polls/display.html',{'data':data})

def update(request):
    if request.method=='POST':
        upform=UpForm(request.POST)
        if upform.is_valid():
            uid=request.POST.get('uid','')
            new_name=request.POST.get('name','')
            if Info.obj.filter(uid=uid):
               ob=Info.obj.filter(uid=uid)
               ob.update(name=new_name)
               messages.info(request,'Name updated Successfully')
               return redirect(update) 
            else:
                messages.info(request,'Invalid uid ... not found in database')
                return redirect(update)
        else:
            messages.info(request,'Data is invalid')
            return redirect(update)
                    
    else:
        upform=UpForm()
        return render(request,'polls/update.html',{'upform':upform})            

def delete(request):
    if request.method=='POST':
        delform=DelForm(request.POST)
        if delform.is_valid():
            uid=request.POST.get('uid','')    
            if Info.obj.filter(uid=uid):
                ob=Info.obj.get(uid=uid)
                ob.delete()
                messages.warning(request,'Record Deleted Successfully')
                return redirect(delete)  
            else:
                messages.warning(request,'Invalid uid ... Not found in database')
                return redirect(delete)  
        else:
            messages.warning(request,'Invalid uid')
            return redirect(delete)
    else:
        delform=DelForm()
        return render(request,'polls/delete.html',{'delform':delform})                 