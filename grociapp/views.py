from django.shortcuts import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import item

from django.shortcuts import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
# from .forms import SignUpForm
from .forms import NewUserForm
from django.db.models import Q
from django.contrib.auth.models import User
# Create your views here

def func(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		else:
			messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render(request, 'index.html' , context={"register_form":form})


def home(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		else:
			messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render(request, 'home.html' , context={"register_form":form})


def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')


def p1(request):
	items = item.objects.all()
	return render(request,'p1.html',{'items':items})

def p2(request):
	return render(request,'p2.html')

def p3(request):
	return render(request,'p3.html')

def p4(request):
	return render(request,'p4.html')

def p5(request):
	return render(request,'p5.html')

def p6(request):
	return render(request,'p6.html')

def p7(request):
	noodles = noodle.objects.all()

	return render(request,'p7.html',{'noodles':noodles})


def vegetables(request):

	items = item.objects.all()

	return render(request,'vegetables.html',{'items':items})



def fruits(request):

	fruits = fruit.objects.all()
	return render(request,'fruits.html',{'fruits':fruits})


def pulses(request):
	pulses = pulse.objects.all()
	return render(request,'pulses.html',{'pulses':pulses})

def spices(request):

	staples = staple.objects.all()

	return render(request,'spices.html',{'staples':staples})


def utensiles(request):

	utensils = utensil.objects.all()

	return render(request,'utensiles.html',{'utensils':utensils})


def disinf(request):

	disinfecents = disinfecent.objects.all()

	return render(request,'disinf.html',{'disinfecents':disinfecents})


def milks(request):

	milks = milk.objects.all()

	return render(request,'milks.html',{'milks':milks})


def biscuits(request):

	biscuits = biscuit.objects.all()

	return render(request,'biscuits.html',{'biscuits':biscuits})


def drinks(request):

	drinks = drink.objects.all()

	return render(request,'drinks.html',{'drinks':drinks})


def noodles(request):

	noodles = noodle.objects.all()

	return render(request,'noodles.html',{'noodles':noodles})



# def signup(request):
# 	return render(request,'signup.html')




def handleSignup(request):
	if request.method=='POST':
		#parameters
		fname=request.POST['fname']
		lname=request.POST['lname']
		Email=request.POST['Email']
		password1=request.POST['password1']
		password2=request.POST['password2']

		#create user
		myuser=User.objects.create_user(username,Email,password)
		myuser.First_Name=fname
		myuser.Last_Name=lname
		myuser.save()
		messages.success(request,"your login successfully ")
		return redirect('home')
		



	else:
		return HttpResponse('404 Not Found')
