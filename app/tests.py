
from itertools import product
from urllib import response
from django.test import SimpleTestCase, TestCase,Client
from django.urls import reverse,resolve
from .models import * 
from app.views import cart, home,order, order_placed

# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_case_home_url(self):
        url=reverse('home')
        self.assertEquals(resolve(url).func,home)
    def test_case_cart_url(self):
        url=reverse('cart')
        self.assertEquals(resolve(url).func,cart)
    def test_case_order_url(self):
        url=reverse('orders')
        self.assertEquals(resolve(url).func,order)
    def test_case_order_placed_url(self):
        url=reverse('order_placed')
        self.assertEquals(resolve(url).func,order_placed)
class TestViews(TestCase):
    def test_case_home(self):
        client=Client()
        url=reverse('home')
        response=client.get(url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'app/home.html')
    def test_case_add_view(self):
        client=Client()
        url=reverse('admin_cart_add')
        response=client.post(url,{
            'user':'piyush',
            'product':'momo',
            'product_qty':'9'
        })
        print(response)
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response,'/admin_cart/')
    # def test_case_cart_edit_view(self):
    #     client=Client()
    #     url=reverse('admin_cart_edit',args=[1])
    #     response=client.post(url,{
    #         'user':'piyush',
    #         'product':'momo',
    #         'product_qty':'9'
    #     })
    #     print(response)
    #     self.assertEquals(response.status_code,302)
    #     self.assertRedirects(response,'/admin_cart/')
    # def test_case_cart_delete_view(self):
    #     client=Client()
    #     newlyCreated=Cart.objects.create(
    #         user="piyush",
    #         product="chicken",
    #         product_qty="4"
    #     )
    #     url=reverse('admin_cart_delete',args=[1])
    #     response=client.delete(url)
    #     print(response)
    #     self.assertEquals(response.status_code,302)
    #     self.assertRedirects(response,'/admin_cart/')
        
