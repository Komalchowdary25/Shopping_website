from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    nomatch=False
    trend=False
    offer=False
    if 'product' in request.GET:
        product=request.GET['product']
        result=ProductsModel.objects.filter(Q(pname__icontains=product) | Q(pdesc__icontains=product) | Q(price__icontains=product) | Q(pcategory__icontains=product))
        if len(result)==0:
            nomatch=True
    elif 'cat' in request.GET:
        cat=request.GET['cat']
        result=ProductsModel.objects.filter(pcategory=cat)
    else:
        result=ProductsModel.objects.all()
    category=[]
    for i in ProductsModel.objects.all():
        if i.pcategory not in category:
            category.append(i.pcategory)
    count=0
    if request.user.is_authenticated:
        cart_count=CartModel.objects.filter(host=request.user)
        for i in cart_count:
            count+=i.quantity
    return render(request,'home.html',{'data':result,'nomatch':nomatch,'category':category,'cart_count':count})

@login_required(login_url='login_')
def addtocart(request,pk):
    product=ProductsModel.objects.get(id=pk)
    try:
        cp=CartModel.objects.get(pname=product.pname,host=request.user)
        cp.quantity+=1
        cp.totalprice+=product.price
        cp.save()
        return redirect('home')
    except:

        CartModel.objects.create(pname=product.pname,
                             price=product.price,
                             pcategory=product.pcategory,
                             quantity=1,
                             totalprice=product.price,
                             pimage=product.pimage,
                             host=request.user)
        return redirect('home')

@login_required(login_url='login_')
def cart(request):
    cart_count=CartModel.objects.filter(host=request.user).count()
    data=CartModel.objects.filter(host=request.user)
    TA=0
    for i in data:
        print(i.totalprice)
        TA+=i.totalprice
    return render(request,'cart.html',{'data':data,'TA':TA,'cart_nav':True,'cart_count':cart_count})

def remove(request,pk):
    cartproduct=CartModel.objects.get(id=pk)
    cartproduct.delete()
    return redirect('cart')

def decrease(request,pk):
    product = CartModel.objects.get(id=pk, host=request.user)
    if product.quantity > 1:
        product.quantity -= 1
        product.totalprice-=product.price
        product.save()
    else:
        product.delete()
    return redirect('cart')

def increase(request,pk):
    product = CartModel.objects.get(id=pk, host=request.user)
    product.quantity += 1
    product.totalprice+=product.price
    product.save()
    return redirect('cart') 

def trending(request):
    a=ProductsModel.objects.filter(trending=True)
    count=0
    if request.user.is_authenticated:
        cart_count=CartModel.objects.filter(host=request.user)
        for i in cart_count:
            count+=i.quantity
    return render(request,'home.html',{'data':a,'trend':True,'cart_count':count})

def offers(request):
    a=ProductsModel.objects.filter(offer=True)
    count=0
    if request.user.is_authenticated:
        cart_count=CartModel.objects.filter(host=request.user)
        for i in cart_count:
            count+=i.quantity
    return render(request,'home.html',{'data':a,'offer':True,'cart_count':count})

def payment(request):
    return render(request,'payment.html')

def knowus(request):
    count=0
    if request.user.is_authenticated:
        cart_count=CartModel.objects.filter(host=request.user)
        for i in cart_count:
            count+=i.quantity
    return render(request,'knowus.html',{'knowus_nav':True,'cart_count':count})

def support(request):
    count=0
    if request.user.is_authenticated:
        cart_count=CartModel.objects.filter(host=request.user)
        for i in cart_count:
            count+=i.quantity
    return render(request,'support.html',{'support_nav':True,'cart_count':count})