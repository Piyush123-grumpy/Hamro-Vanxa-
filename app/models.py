import datetime
import os
from django.db import models
from account.models import Account

# Create your models here.

def get_file_path(request, filename):
    original_filename=filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s"%(nowTime, original_filename)
    return os.path.join('uploads/',filename)

class Category(models.Model):
    name = models.CharField( max_length=150, null=False, blank=False)
    image=models.ImageField( upload_to='shop/cat_images', null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey("Category",on_delete=models.CASCADE)
    name = models.CharField( max_length=150, null=False, blank=False)
    product_image=models.ImageField(default='', null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    Todays_detail = models.BooleanField(default=False, help_text="0=defeault, 1=Todays_detail")
    All_time_special= models.BooleanField(default=False, help_text="0=defeault, 1=Trending")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product.name
    @property
    def total_cost(self):
        return self.product_qty * self.product.selling_price
class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False,default=1)
    order_status=(
        ('Placed','Placed'),
        ('Pending','Pending'),
        ('In progress','In progress'),
        ('Delivered','Delivered'),

    )
    status=models.CharField(max_length=100,choices=order_status)
    
    def __str__(self):
        return self.product.name
class Favo(models.Model):
    user = user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)