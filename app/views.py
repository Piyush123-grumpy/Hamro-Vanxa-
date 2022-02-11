from django.shortcuts import render
from .models import *
from django.db.models import Q


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

def mobile(request):
 return render(request, 'app/mobile.html')

# def login(request):
#  return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
