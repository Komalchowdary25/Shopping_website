from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from base.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def login_(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        auth_user=authenticate(username=username,password=password)
        if auth_user:
            login(request,auth_user)
            return redirect('home')
        else:
            return render(request,'login_.html',{'error':'Username or password are incorrect..!!'})
    return render(request,'login_.html',{'login_nav':True})

@login_required(login_url='login_')
def profile(request):
    count=0
    cart_count=CartModel.objects.filter(host=request.user)
    for i in cart_count:
        count+=i.quantity
    return render(request,'profile.html',{'profile_nav':True,'cart_count':count})

def register(request):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        try:
            a=User.objects.get(username=username)
            return render(request,'register.html',{'error':'Username already exists..!!'})
        except:
            a=User.objects.create(first_name=first_name,last_name=last_name,email=email,username=username)
            a.set_password(password)
            a.save()
        return redirect('login_')
    return render(request,'register.html',{'register_nav':True})

def logout_(request):
    logout(request)
    return redirect('login_')

@login_required(login_url='login_')
def update_profile(request):
    if request.method=='POST':
        request.user.first_name=request.POST['fname']
        request.user.last_name=request.POST['lname']
        request.user.email=request.POST['email']
        request.user.save()
        return redirect('profile')
    count=0
    cart_count=CartModel.objects.filter(host=request.user)
    for i in cart_count:
        count+=i.quantity
    return render(request,'update_profile.html',{'update_profile_nav':True,'cart_count':count})

@login_required(login_url='login_')
def reset_password(request):
    user=request.user
    if request.method=='POST':
        if 'oldpassword' in request.POST:
            old_password=request.POST['oldpassword']
            auth_user=authenticate(username=user.username,password=old_password)
            if auth_user:
                return render(request,'reset_password.html',{'new_pass':True,'reset_password_nav':True})
            else:
                return render(request,'reset_password.html',{'error':'Entered wrongPassword'})
        if 'newpassword' in request.POST:
            new_password=request.POST['newpassword']
            if user.check_password(new_password):
                return render(request,'reset_password.html',{'error':'Password should not be same as old password..!!'})
            user.set_password(new_password)
            user.save()
            return redirect('login_')
    count=0
    cart_count=CartModel.objects.filter(host=request.user)
    for i in cart_count:
        count+=i.quantity
    return render(request,'reset_password.html',{'reset_password_nav':True,'cart_count':count})

def forget_password(request):
    if request.method=='POST':
        username=request.POST['username']
        try:
            u=User.objects.get(username=username)
            request.session['fp_user']=u.username
            return redirect('new_password')
        except User.DoesNotExist:
            return render(request,'forget_password.html',{'error':'User doesnot exists..!!'})
    return render(request,'forget_password.html',{'forget_password_nav':True})

def new_password(request):
    username=request.session.get('fp_user')
    if username is None:
        return redirect('forget_password')
    user=User.objects.get(username=username)
    if request.method=='POST':
        new_password=request.POST['newpassword']
        if user.check_password(new_password):
            return render(request,'new_password.html',{'similar':'Oldpassword should not be same as new password..'})
        user.set_password(new_password)
        user.save()
        del request.session['fp_user']
        return redirect('login_')
    return render(request,'new_password.html',{'new_password_nav':True})
