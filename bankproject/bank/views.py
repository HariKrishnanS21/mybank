from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import pdet,District,Branch
from django.views.generic import CreateView

from django.http import JsonResponse



# Create your views here.
def home(request):
    return render(request,'home.html')

def forms(request):
    if request.method == 'POST':
        name=request.POST['name']
        dob=request.POST['dob']
        age=request.POST['age']
        mob=request.POST['mob']
        mail=request.POST['mail']
        address=request.POST['address']
        person=pdet(name=name,dob=dob,age=age,mob=mob,mail=mail,address=address)
        person.save()
        messages.info(request,"information added successfully")
        return redirect('bank:success')


    district = District.objects.all()
    return render(request,'forms.html',{'district':district})

def get_json_district(request):
    dist_val=list(District.objects.values())
    return JsonResponse({'data':dist_val})

def get_branches(request, *args, **kwargs):
    selected_dist = kwargs.get('district')
    branch_val = list(Branch.objects.filter(district__id=selected_dist).values())
    return JsonResponse({'data':branch_val})

def success(request):
    details = pdet.objects.all()
    return render(request,'success.html',{'details':details})


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        u=auth.authenticate(username=username,password=password)

        if u is not None:
            auth.login(request,u)
            return redirect('bank:forms')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('bank:login')
    return render(request,'login.html')

def register(request):
    if request.method== 'POST':
        uname=request.POST['uname']
        password=request.POST['pass']
        cpass=request.POST['cpass']

        if password == cpass:
            if User.objects.filter(username=uname):
                print("username")
                # messages.info(request,"Username already exist")
                return redirect('bank:register')
            else:
                user=User.objects.create_user(username=uname,password=password)
                user.save()
                print("user")
                # messages.info(request,"user successfully created")
        else:
            print("pass")
            # messages.info(request,"passwords are not  matching")
            return redirect('bank:register')
        return redirect('bank:login')

    return render(request,'reg.html')

def logout(request):
    auth.logout(request)
    return redirect('/')




