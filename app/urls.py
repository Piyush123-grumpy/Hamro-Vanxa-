from django.urls import path
from app import views
from app.controller import authview
urlpatterns = [
     path('', views.home),
    #  path('product-detail/', views.product_detail, name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('login/', authview.loginpage, name='loginpage'),
    path('registration/', authview.register, name='customerregistration'),
    path('logout/', authview.logoutpage, name='logout'),
    path('checkout/', views.checkout, name='checkout'),
    path('products/<int:myid>', views.productview, name="products"),
]
