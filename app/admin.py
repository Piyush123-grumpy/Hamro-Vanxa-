from django.contrib import admin
from app.models import *
# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display=['category','name','product_image','description','original_price','selling_price','Todays_detail','All_time_special']
admin.site.register(Product,AdminProduct)
admin.site.register(Order)
admin.site.register(Favo)
admin.site.register(Cart)
admin.site.register(Category)

