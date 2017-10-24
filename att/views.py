from django.shortcuts import render,redirect
from .forms import attform
from django.contrib.auth import authenticate,login,logout
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
                return redirect('att:attviewauth')

    return render(request,'login.html')



def index(request):
    return render(request,'index.html')





def attview(request):
    context={
        'all_entries':attsheet.objects.all(),

    }
    return render(request,'all.html',context)


def attviewauth(request):
    if request.user.is_authenticated():
        context = {
        'all_entries': attsheet.objects.all(),

        }
        return render(request, 'auth.html', context)

    return redirect('att:auth_login')

def approveit(request,attsheet_id):
    currentsheet = attsheet.objects.get(pk=attsheet_id)
    currentsheet.approved=True

    currentsheet.save()
    msg=" approved successfully!"
    context = {
        'all_entries': attsheet.objects.all(),
        'success_message':msg,
        'sheet':currentsheet,
        'approvance':True,
    }
    return render(request,'auth.html',context)

def rejectit(request,attsheet_id):
    currentsheet = attsheet.objects.get(pk=attsheet_id)
    currentsheet.rejected=True

    currentsheet.save()
    msg=" rejected!"
    context = {
        'all_entries': attsheet.objects.all(),
        'success_message':msg,
        'sheet':currentsheet,
        'rejected':True,
    }
    return render(request,'auth.html',context)


def writerem(request,attsheet_id):
    if request.method=="GET":
        return redirect('att:attviewauth')

    currentsheet = attsheet.objects.get(pk=attsheet_id)

    remark = request.POST.get('remarks', None)
    currentsheet.remarks = remark
    currentsheet.save()
    return redirect('att:attviewauth')



def log_out(request):
    logout(request)
    return redirect('att:index')
