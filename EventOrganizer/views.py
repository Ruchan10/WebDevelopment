from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here
# creating function to return files
allimages = on.objects.all()  

data = rev.objects.all() 

dat = {
    "da": data,
    "on":allimages
}

def login_page(request):
    if request.method=="POST":
        user=authenticate(request,
        username=request.POST['username']
        ,password=request.POST['password'])
        if user is not None:
            login(request,user)
            messages.success(request, 'User logged in!')
            return redirect("/")
        else:
            messages.error(request, 'Invalid Username or Password.')
            return redirect("logIn")
    else:
        return render(request,"login.html")


def signup(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        psw=request.POST.get('psw')
        pswRepeat=request.POST.get('pswRepeat')

        if User.objects.filter(username=uname):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('signUp')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signUp')
        
        if len(uname)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signUp')
        
        if psw != pswRepeat:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signUp')


        myuser=User.objects.create_user(uname,email,psw)
        myuser.uName=uname
        myuser.is_active=True
        myuser.save()
        messages.success(request,"your account has been created,now login")
        
        return redirect('logIn')
    return render(request, 'signup.html')
    

def signout(request):
    logout(request)
    messages.success(request, "LOGGED OUT")
    return redirect('home.html')

def home(request):
    if request.method=='POST':
        if request.POST.get('name'):
            table=contact()
            table.id=1
            table.name=request.POST.get('name')
            table.email=request.POST.get('email')
            table.number=request.POST.get('number')
            table.subject=request.POST.get('subject')
            table.message=request.POST.get('message')
            table.save()
        return redirect('homePage')
    return render(request,'home.html',dat)

def revie(request):
    if request.method=='POST':
        if request.POST.get('textArea'):
            table=rev()
            table.user="rk10"
            table.description=request.POST.get('textArea')
            table.rating=request.POST.get('rate')
            table.save()
        return redirect('homePage')
    return render (request, 'review.html')

def ongoing(request):
    print(request.FILES)
    if request.method=='POST':
        if request.POST.get('name'):
            table=on()
            table.name=request.POST.get('name')
            table.img=request.FILES['image']
            table.address=request.POST.get('Address')
            table.time=request.POST.get('Time')
            table.descr=request.POST.get('desc')
            table.save()
        return redirect('homePage')
    return render(request, 'ongoing.html')
