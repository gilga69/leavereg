from django.shortcuts import render,redirect
from .forms import attform
from django.contrib.auth import authenticate,login
from .models import attsheet

def attendancereg(request):
    attsheetform=attform(request.POST)
    s_message="Success! Your response has been recorded!"
    e_message="Please fill all the fields properly!"
    if attsheetform.is_valid():
        attsheetform.save()
        context={
            'success_message': s_message,

        }
        return render(request,'success.html',context)

    else:
        context={
        'attform':attsheetform,
        'error_message':e_message
    }
        return render(request,'error.html',context)


def ulogin(request):
    if request.method=='POST':
        username=request.POST.get('username',None)
        password=request.POST.get('password',None)
        guest=authenticate(username=username,password=password)

        if guest is not None:
            if guest.is_active:
                login(request,guest)
                return redirect('att:attview')

    return render(request,'login.html')



def index(request):
    return render(request,'index.html')





def attview(request):


    context={
        'all_entries':attsheet.objects.all(),
    }
    return render(request,'all.html',context)
