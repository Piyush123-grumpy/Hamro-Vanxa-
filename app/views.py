from itertools import product
from unicodedata import category
from urllib import request
from django.shortcuts import render,redirect
from account.models import Account
from django.contrib.auth.models import User 
from .models import * 
from app.forms import *
from django.db.models import Q
from django.http import JsonResponse
from django.contrib import messages
import json


def home(request):
    product=Product.objects.all()
    context={"product":product}
    return render(request, 'app/home.html',context)
def admin_cart(request):
    if request.user.is_authenticated:
        if request.user.is_admin==True:
            cart=Cart.objects.all()
            return render(request,'app/admin_cart.html',{'cart':cart})
    return render(request,'app/404.html')
def admin_cart_edit(request,cart_id):
    cart=Cart.objects.get(id=cart_id)
    user=Account.objects.all()
    product=Product.objects.all()
    if request.user.is_authenticated & request.user.is_admin==True:    
        if(request.method=="POST"):
            print(request.POST)
            form=CartForm(request.POST,instance=cart)

            if form.is_valid():
                print("valid")
                form.save()
            else:
                print("invalid")

            return redirect('/admin_cart/')
        else:
            return render(request,'app/edit.html',{'cart':cart,'user':user,'product':product})
    return render(request,'app/404.html')
def admin_cart_add(request):
    user=Account.objects.all()
    product=Product.objects.all()
    if request.user.is_authenticated & request.user.is_admin==True: 
        if(request.method=="POST"):
            print(request.POST)
            form=CartForm(request.POST,request.FILES)

            if form.is_valid():
                print("valid")
                form.save()
            else:
                print("invalid")

            return redirect('/admin_cart/')
        else:
            return render(request,'app/cart_add.html',{'cart':cart,'user':user,'product':product})
    return render(request,'app/404.html')
def admin_category_edit(request,category_id):
    category=Category.objects.get(id=category_id)
    if request.user.is_authenticated & request.user.is_admin==True: 
        if(request.method=="POST"):
            print(request.POST)
            form=CategoryForm(request.POST,request.FILES,instance=category)

            if form.is_valid():
                print("valid")
                form.save()
            else:
                print("invalid")

            return redirect('/admin_category/')
        else:
            return render(request,'app/category_edit.html',{'category':category})
    return render(request,'app/404.html')
def admin_category_add(request):
    if request.user.is_authenticated & request.user.is_admin==True:
        if(request.method=="POST"):
            print(request.POST)
            form=CategoryForm(request.POST)

            if form.is_valid():
                print("valid")
                form.save()
            else:
                print("invalid")

            return redirect('/admin_category/')
        else:
            return render(request,'app/category_add.html')
    return render(request,'app/404.html')
def admin_order_edit(request,order_id):
    order=Order.objects.get(id=order_id)
    user=Account.objects.all()
    product=Product.objects.all()
    if request.user.is_authenticated & request.user.is_admin==True:
        if(request.method=="POST"):
            print(request.POST)
            form=OrderForm(request.POST,instance=order)

            if form.is_valid():
                print("valid")
                form.save()
            else:
                print("invalid")

            return redirect('/admin_order/')
        else:
            return render(request,'app/order_edit.html',{'order':order,'user':user,'product':product})
    return render(request,'app/404.html')
def admin_order_add(request):
    user=Account.objects.all()
    product=Product.objects.all()
    if request.user.is_authenticated & request.user.is_admin==True:
        if(request.method=="POST"):
            print(request.POST)
            form=OrderForm(request.POST)

            if form.is_valid():
                print("valid")
                form.save()
            else:
                print("invalid")

            return redirect('/admin_order/')
        else:
            return render(request,'app/order_add.html',{'order':order,'user':user,'product':product})
    return render(request,'app/404.html')
def admin_product_edit(request,product_id):
    product=Product.objects.get(id=product_id)
    category=Category.objects.all()
    if request.user.is_authenticated & request.user.is_admin==True:
        if(request.method=="POST"):
            print(request.POST)
        
            form=ProductForm(request.POST,request.FILES,instance=product)

            if form.is_valid():
                print("valid")
                form.save()
            else:
                print("invalid")

            return redirect('/admin_product/')
        else:
            return render(request,'app/product_edit.html',{'category':category,'product':product})
    return render(request,'app/404.html')
def admin_product_add(request):
    category=Category.objects.all()
    if request.user.is_authenticated & request.user.is_admin==True:
        if(request.method=="POST"):
            print(request.POST)
        
            form=ProductForm(request.POST,request.FILES)

            if form.is_valid():
                print("valid")
                form.save()
            else:
                print("invalid")

            return redirect('/admin_product/')
        else:
            return render(request,'app/product_add.html',{'category':category})
    return render(request,'app/404.html')
    
def admin_product(request):
    if request.user.is_authenticated & request.user.is_admin==True:
        product=Product.objects.all()
        return render(request,'app/admin_product.html',{'product':product})
    return render(request,'app/404.html')
def admin_category(request):
    if request.user.is_authenticated & request.user.is_admin==True:
        category=Category.objects.all()
        return render(request,'app/admin_category.html',{'category':category})
    return render(request,'app/404.html')
def admin_order(request):
    if request.user.is_authenticated & request.user.is_admin==True:
        order=Order.objects.all()
        return render(request,'app/admin_order.html',{'order':order})
    return render(request,'app/404.html')
def admin_cart_delete(request,cart_id):
    if request.user.is_authenticated & request.user.is_admin==True:
        cart=Cart.objects.get(id=cart_id)
        cart.delete()
        return redirect('/admin_cart/')
    return render(request,'app/404.html')
def admin_category_delete(request,category_id):
    if request.user.is_authenticated & request.user.is_admin==True:
        category=Category.objects.get(id=category_id)
        category.delete()
        return redirect('/admin_category/')
    return render(request,'app/404.html')
def admin_order_delete(request,order_id):
    if request.user.is_authenticated & request.user.is_admin==True:
        order=Order.objects.get(id=order_id)
        order.delete()
        return redirect('/admin_order/')
    return render(request,'app/404.html')
def admin_product_delete(request,product_id):
    if request.user.is_authenticated & request.user.is_admin==True:
        product=Product.objects.get(id=product_id)
        product.delete()
        return redirect('/admin_product/')
    return render(request,'app/404.html')
def productview(request,myid):
    if request.user.is_authenticated:
        products=Product.objects.filter(id=myid)
        product=Product.objects.get(id=myid)
        print(products)
        item_already_in_Cart=False
        item_already_in_Cart=Cart.objects.filter(Q(product=product)& Q(user=request.user)).exists()
        context={'products':products[0],'item_already_in_Cart':item_already_in_Cart}
        return render(request, 'app/productdetail.html',context)
    else:
        messages.warning(request,"You Have to Login First")
        return redirect('loginpage')
def update_item(request):
    data=json.loads(request.body)
    productId=data['productId']
    Category=data['category']
    action=data['action']
    print('Action:',action)
    print('productId:',productId)
    product=Product.objects.get(id=productId)
    user=request.user
    cart,created=Cart.objects.get_or_create(user=user ,product=product)
    if action=='add':
        cart.product_qty=(cart.product_qty + 1)
    elif action=='remove':
        cart.product_qty = (cart.product_qty - 1)
    cart.save()
    if cart.product_qty<=0:
        cart.delete()
    return JsonResponse('Item was added',safe=False)

def cart(request):
    if request.user.is_authenticated:
        user=request.user
        carts=Cart.objects.filter(user=user)
        amount=0.0
        
        shipping_amount=70.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==user ]
        if cart_product:
            for p in cart_product:
                tempamount=(p.product_qty* p.product.selling_price)
                amount+=tempamount
                total_amount=amount+shipping_amount
            return render(request,'app/cart.html',{"carts":carts,"total_amount":total_amount,"amount":amount})
        else:
            return render(request,'app/emptycart.html')

    else:
        return render(request,'app/emptycart.html')
def plus_cart(request):
    if request.method=='GET':
        user=request.user
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.product_qty+=1
        c.save()
        amount=0.0
        shipping_amount=70.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==user ]
        for p in cart_product:
            tempamount=(p.product_qty * p.product.selling_price)
            amount+=tempamount
        data={
            'quantity':c.product_qty,
            'amount':amount,
            'totalamount':amount + shipping_amount
            }
        return JsonResponse(data)
def minus_cart(request):
    if request.method=='GET':
        user=request.user
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.product_qty-=1
        if c.product_qty<=0:
            c.delete()
        else:
            c.save()
        amount=0.0
        shipping_amount=70.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==user ]
        for p in cart_product:
            tempamount=(p.product_qty * p.product.selling_price)
            amount+=tempamount
        data={
            'quantity':c.product_qty,
            'amount':amount,
            'totalamount':amount + shipping_amount
            }
        return JsonResponse(data)
def remove_cart(request):
    if request.method=='GET':
        user=request.user
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.delete()
        amount=0.0
        shipping_amount=70.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==user ]
        for p in cart_product:
            tempamount=(p.product_qty * p.product.selling_price)
            amount+=tempamount
        data={
            'amount':amount,
            'totalamount':amount + shipping_amount
            }
        return JsonResponse(data)
def buy_now(request,buy_id):
    product=Product.objects.filter(id=buy_id)
    add=request.user
    print(add)
    return render(request, 'app/buynow.html',{"product":product,"add":add})

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def order_placed(request):
    user=request.user
    cart=Cart.objects.filter(user=user)
    for c in cart:
        Order(user=user,product=c.product,product_qty=c.product_qty,status="Placed").save()
        c.delete()
    return redirect('orders')
def order(request):
    order=Order.objects.all()
    user=request.user
    return render(request,'app/orders.html',{'order':order,'user':user})

def change_password(request):
 return render(request, 'app/changepassword.html')

def burger(request):
    product=Product.objects.filter(category="3")
    context={"product":product}
    return render(request, 'app/burger.html',context)
def pizza(request):
    product=Product.objects.filter(category="3")
    context={"product":product}
    return render(request, 'app/pizza.html',context)
def chicken(request):
    product=Product.objects.filter(category="1")
    context={"product":product}
    return render(request, 'app/chicken.html',context)
def momo(request):
    product=Product.objects.filter(category="4")
    context={"product":product}
    return render(request, 'app/momo.html',context)
def beer(request):
    product=Product.objects.filter(category="6")
    context={"product":product}
    return render(request, 'app/beer.html',context)
def alcohol(request):
    product=Product.objects.filter(category="5")
    context={"product":product}
    return render(request, 'app/alcohol.html',context)
def wine(request):
    product=Product.objects.filter(category="7")
    context={"product":product}
    return render(request, 'app/wine.html',context)

# def login(request):
#  return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

def checkout(request):
    user=request.user
    add=Account.objects.all()
    print(add)
    cart_items=Cart.objects.filter(user=user)
    amount=0.0
    shipping_amount=70.0
    total_amount=0.0
    cart_product=[p for p in Cart.objects.all() if p.user==user ]
    if cart_product:
        for p in cart_product:
            tempamount=(p.product_qty * p.product.selling_price)            
            amount+=tempamount
        total_amount=amount+shipping_amount
    return render(request,'app/checkout.html',{'cart_items':cart_items, 'add':add,'total_amount':total_amount})
def search(request):
    q=request.GET['q']
    products=Product.objects.filter(name__icontains=q).order_by('-id')
    context={'products':products}
    return render(request,'app/search.html/',context)