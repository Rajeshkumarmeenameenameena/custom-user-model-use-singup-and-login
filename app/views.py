from django.shortcuts import render,HttpResponse, redirect
from .models import studentnew
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout


# Create your views 

def homepage(request):
    return render (request,'home.html')
def singuppage(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        passwordagain=request.POST['passwordagain']
        phoneno=request.POST['phoneno']
        age=request.POST['age']
        gender=request.POST['gender']
        birth=request.POST['birth']
        if password==passwordagain:
            try:
                a=User.objects.get(username=name)
                return render(request,'singup.html',{'error':'already exist'})
            #after login we send home page
                
            except User.DoesNotExist:
                stu=User.objects.create_user(username=name,email=email,password=password)
                mod=studentnew.objects.create(phoneno=phoneno,age=age,gender=gender,birtdate=birth,User=stu)
                mod.save()
                stu.save()
                return redirect('login')
        else:
            return render(request,'singup.html',{'error':'password does not match'})
        
    return render(request,'singup.html')



def loginpage(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        # print(email,password)
        # a=student.objects.get(email=email)
        # print(a.email)
        # print(a.name)
        # print(a.password)
        user= authenticate(request,username=name,password=password)
        print(user)
        if user is not None:
           return redirect('home')
        else:
            return render(request,'login.html')
            
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')

