from unicodedata import category
from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.http import JsonResponse
import json


def home(request):
    product=Product.objects.all()
    context={"product":product}
    return render(request, 'app/home.html',context)

def productview(request,myid):
    products=Product.objects.filter(id=myid)
    product=Product.objects.get(id=myid)
    print(products)
    item_already_in_Cart=False
    item_already_in_Cart=Cart.objects.filter(Q(product=product)& Q(user=request.user)).exists()
    context={'products':products[0],'item_already_in_Cart':item_already_in_Cart}
    return render(request, 'app/productdetail.html',context)
def update_item(request):
    data=json.loads(request.body)
    productId=data['productId']
    Category=data['category']
    action=data['action']
    print('Action:',action)
    print('productId:',productId)
    customer = request.user.customer
    product=Product.objects.get(id=productId)
    
    cart,created=Cart.objects.get_or_create(category=Category,product=Product)
    if action=='add':
        cart.quantity=(cart.quantity + 1)
    elif action=='remove':
        cart.quantity = (cart.quantity - 1)
    cart.save()
    if cart.quantity<=0:
        cart.delete()
    return JsonResponse('Item was added',safe=False)

def add_to_cart(request):

 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def burger(request):
    product=Product.objects.filter(category="3")
    context={"product":product}
    return render(request, 'app/burger.html',context)
def pizza(request):
    product=Product.objects.filter(category="8")
    context={"product":product}
    return render(request, 'app/pizza.html',context)
def chicken(request):
    product=Product.objects.filter(category="7")
    context={"product":product}
    return render(request, 'app/chicken.html',context)
def momo(request):
    product=Product.objects.filter(category="6")
    context={"product":product}
    return render(request, 'app/momo.html',context)
def beer(request):
    product=Product.objects.filter(category="2")
    context={"product":product}
    return render(request, 'app/beer.html',context)
def alcohol(request):
    product=Product.objects.filter(category="4")
    context={"product":product}
    return render(request, 'app/alcohol.html',context)
def wine(request):
    product=Product.objects.filter(category="5")
    context={"product":product}
    return render(request, 'app/wine.html',context)

# def login(request):
#  return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
