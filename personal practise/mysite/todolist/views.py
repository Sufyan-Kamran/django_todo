from django.shortcuts import render
from django.http import HttpResponse
from .models import user,todo,donetask,notice
from datetime import date
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login as authlogin, logout as authlogout
from django.contrib import messages 
import datetime

# Create your views here.

def index(request):
    return redirect('login')
def action(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            fname = request.user.username#request.POST.get('fname')
            #lname = request.POST.get('password')
            #uid = user.objects.filter(fname=fname)
            #fetch = user.objects.get(id=1)
            notices = notice.objects.filter(username='lubna')
            uid = user.objects.filter(fname=request.user.username)
            fetch = user.objects.get(username=request.user.username)
            fname1 = fetch.fname
            tasks = todo.objects.filter(uid=fetch.id)
            donetasks = donetask.objects.filter(uid=fetch.id)
            if fname == fname1:# and lname ==lname1:
                params = {"u":uid,"f":fetch, "e":tasks, "donet":donetasks,'notice':notices}  
                logged = "loggedin"
                return render(request,"todolist/action.html",params)
            else:
                #print(fname1, lname1,"Sorry")
                return HttpResponse("Invalid")
        else:
            return redirect('login')
    else:
        return redirect('login')
def task(request):
    tid = request.POST.get('tid')
    uid = request.POST.get('uid')
    tname = request.POST.get('tname')
    task = request.POST.get('task')
    ntname = request.POST.get('ntname')
    ntask = request.POST.get('ntask')   
    #fetch = user.objects.get(id=1)
    fetch = user.objects.get(username=request.user.username)
    taskfetch = todo.objects.get(id=tid)
    d = datetime.date(1997, 10, 19)
    if fetch.fname != "" and uid != "" and tname != "" and task != "": 
        data = donetask(fname=fetch.fname,uid=uid,tname=tname,task=task,status="Completed",tdate=d)
        data.save()
        taskfetch = todo.objects.get(id=tid)
        taskfetch.delete()
        return render(request,"todolist/action.html")     
    else:
        return render(request,"todolist/action.html")
    
    return render(request,"todolist/action.html")
    #return HttpResponse(f"{uid}{tname}{task}{tid}{fetch.id,fetch.fname,fetch.lname}{uid,taskfetch.tid,taskfetch.fname,taskfetch.uid,taskfetch.tname,taskfetch.task,taskfetch.status,}")
def donetasks(request):
    donetask = donetask.objects.all()
    param = {"donet":donetask}
    return render(request,"todolist/action",params)
def new(request):
    if request.method == "POST":
        uid = request.POST.get('uid')
        ntname = request.POST.get('ntname')
        ntask = request.POST.get('ntask')
        ufetch = user.objects.get(id=uid)
        data = todo(fname=ufetch.fname,uid=ufetch.id,tname=ntname,task=ntask,status="Pending")
        data.save()
        return render(request,"todolist/new.html")    
    return render(request,"todolist/new.html")    
def delete(request):
    tid = request.POST.get('tid')
    taskfetch = todo.objects.get(id=tid)
    taskfetch.delete()
    return redirect('action')
def preview(request,id):
    tfetch = donetask.objects.get(id=id)
    uid = user.objects.filter(fname=tfetch.fname)
    param = {"ee":tfetch,"u":uid}
    #return HttpResponse(f"{tfetch.tname}")
    return render(request,"todolist/preview.html", param)
def about(request):
    return render(request,"todolist/about.html")
def contact(request):
    return render(request,"todolist/contact.html")
def register(request):
    if request.method=="GET":
        return render(request,"todolist/register.html")
    if request.method =="POST":
        username= request.POST.get('username')
        email=request.POST.get('email')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        pass1=request.POST.get('password')
        pass2=request.POST.get('cpassword')
        # Create the user
        users = user(username=username,fname=fname,lname=lname,email=email,password=pass1)
        users.save()
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        return render(request,"todolist/register.html")
    return render(request,"todolist/register.html")
def login(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['username']
        loginpassword=request.POST['password']
        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            authlogin(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("action")
        else:
            return redirect('login')
            print(loginpassword,loginusername)
            messages.error(request, f"{loginpassword,loginusername}")
            return redirect("action")
    return render(request,"todolist/login.html")
    
   

    return HttpResponse("login")
def logout(request):
    if request.user.is_authenticated:
        print("User is logged in :)")
        print(f"Username --> {request.user.username}")
    else:
        print("User is not logged in :(")
    authlogout(request)
    return redirect('/todolist/login/')

def notices(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            uid = request.user.id
            usernames = request.user.username
            notices = request.POST.get('notice')
            notice_titles = request.POST.get('notice_title')
            comp = datetime.date(1997, 10, 19)
            year = comp.year
            month = comp.month
            day =  comp.day
            date = f"{year}-{month}-{day}"
            notice_data = notice(uid=uid,username= usernames,notice_title=notice_titles,notice=notices,notice_date=date,expiry_date=date,completion_date=date)
            notice_data.save()
            #print(f"{uid,username,notice,notice_title,d}")
            return redirect('notice')
        return render(request,"todolist/notice.html")
    else:
        return render(request,"todolist/login.html")