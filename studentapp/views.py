from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control, never_cache

from studentapp.models import City, Course, Student


# Create your views here.
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def reg_fun(request):
    return render(request,'register.html',{'data':''})

@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def regdata_fun(request):
    u_name=request.POST['rgname']
    u_email=request.POST['rgemail']
    u_password=request.POST['rgpassword']

    if User.objects.filter(Q(username=u_name) | Q(email=u_email)).exists():
        return render(request, 'register.html',{'data':'Usr_name,email and password is already exists !!!!'})
    else:
        u1 = User.objects.create_superuser(username=u_name,email=u_email,password=u_password)
        u1.save()
        return redirect('login')


@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def log_fun(request):
    return render(request,'login.html',{'data':''})

@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def logdata(request):
    u_name = request.POST['rgname']
    u_password = request.POST['rgpassword']
    user1 = authenticate(username=u_name,password=u_password)
    if user1 is not None:
        if user1.is_superuser:
            login(request,user1)
            return redirect('home')
        else:
            return render(request,'login.html',{'data':'User is not a super user..'})
    else:
        return render(request, 'login.html', {'data': 'Enter proper user_name and password..'})
@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def home(request):
    return render(request,'home.html')
@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def add_stu_fun(request):
    city=City.objects.all()
    course=Course.objects.all()
    return render(request,'addstudent.html',{'city_name':city,'course_name':course})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def reddata_fun(request):
    s1=Student()
    s1.Student_name=request.POST['tbname']
    s1.Student_age=request.POST['tbage']
    s1.Student_ph=request.POST['tbmob']
    s1.Student_city=City.objects.get(city=request.POST['ddlcity'])
    s1.Student_course=Course.objects.get(course=request.POST['ddlcourse'])
    s1.save()
    return redirect('add')




@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def display(request):
    s=Student.objects.all()
    return render(request,'display.html',{'data':s})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def update(request,id):
    c=Student.objects.get(id=id)
    city = City.objects.all()
    course=Course.objects.all()
    if request.method=='POST':
        c.Student_name =request.POST['tbname']
        c.Student_age = request.POST['tbage']
        c.Student_ph = request.POST['tbmob']
        c.Student_city = City.objects.get(city=request.POST['ddlcity'])
        c.Student_course = Course.objects.get(course=request.POST['ddlcourse'])
        c.save()
        return redirect('dis')
    return render(request,'update.html',{'data':c,'Course_name':course,'City_name':city})
@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def delete(request,id):
    c=Student.objects.get(id=id)
    c.delete()
    return redirect('dis')

@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def log_out(request):
    logout(request)
    return redirect('login')