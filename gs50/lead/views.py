from django import forms
from django.contrib.auth import authenticate
from django.http import request
from django.http.request import RawPostDataException
from django.shortcuts import redirect, render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm, LeadForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . models import Lead
from django.shortcuts import get_object_or_404, get_list_or_404
# Create your views here.



#this function will update/edit
def update_data(request , id):
    if request.method == 'POST':
        lead = Lead.objects.get(pk=id)
        form = LeadForm(request.POST)
        leads = Lead.objects.filter(user=request.user)
        if form.is_valid():
            lead.name = form.cleaned_data['name']
            lead.company_name =form.cleaned_data['company_name']
            lead.save()
            return redirect('mylead')
    else:
        form = LeadForm()
    return  render(request, 'lead/updatelead.html',{'form':form},
    {'leads':leads})



#delete functions
def delete_lead(request, id):
    if request.method == 'POST':
     pi = Lead.objects.get(pk=id)
     pi.delete()
     return redirect('mylead')


def mylead(request):
    lead = Lead.objects.filter(user=request.user)
    return render(request, 'lead/leadlist.html',{'lead':lead})


def create_lead(request):
    if request.method == 'POST':
        fm = LeadForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            cm = fm.cleaned_data['company_name']
            reg = Lead(name = nm,company_name=cm)
            reg.user = request.user
            reg.save() 
            #lead = Lead.objects.filter(user=request.user)
            return redirect('mylead')
            #fm = LeadForm()
    else:
        fm = LeadForm()
    return render(request, 'lead/dashbord.html', {'form':fm})




def home(request):
    return render(request, 'lead/home.html')



def user_singup(request):
    if request.method == "POST":
     form = SignUpForm(request.POST)
     if form.is_valid():
        messages.success(request, 'congration ')
        form.save()
        return redirect('Login')
    else:
      form = SignUpForm()
    return render(request, 'lead/singup.html',{'form':form})




def Login(request):
 if not request.user.is_authenticated:
    if request.method == "POST":
     form  = LoginForm(request=request, data=request.POST)
     if form.is_valid():
        uname = form.cleaned_data['username']
        upass = form.cleaned_data['password']
        user = authenticate(username= uname, password=upass)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfully')
            return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
    form = LoginForm()
    return render(request, 'lead/login.html',{'form':form})
 else:
      return HttpResponseRedirect('/dashboard/')



#logout
def Logout(request):
  logout(request)
  return HttpResponseRedirect('/')



