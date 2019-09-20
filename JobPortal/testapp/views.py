from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from testapp.models import *
from django.http import HttpResponseRedirect

# Create your views here.
def start(request):
    return render(request,'testapp/start.html')

def index1(request):
    return render(request,'testapp/index.html')

def login1(request):
    return render(request,'registration/login.html')

def login(request):
    return render(request, 'useraccounts/login.html')


def home_view(request):
    return render(request,'testapp/home.html')

# @login_required
def hydjobs1(request):
    job_list=hydjobs.objects.order_by('-date')
    paginator=Paginator(job_list,10)
    page_number=request.GET.get('page')
    try:
        job_list=paginator.page(page_number)
    except PageNotAnInteger:
        job_list=paginator.page(1)
    except EmptyPage:
        job_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/hydjobs.html',{'job_list':job_list})

def blorejobs1(request):
    job_list=blorejobs.objects.order_by('-date')
    paginator=Paginator(job_list,10)
    page_number=request.GET.get('page')
    try:
        job_list=paginator.page(page_number)
    except PageNotAnInteger:
        job_list=paginator.page(1)
    except EmptyPage:
        job_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/blorejobs.html',{'job_list':job_list})

def punejobs(request):
    return render(request,'testapp/punejobs.html')

def chennaijobs(request):
    return render(request,'testapp/chennaijobs.html')

def signup_view1(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
    if form.is_valid():
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})

def logout_view(request):
    return render(request,'testapp/customlogout.html')
