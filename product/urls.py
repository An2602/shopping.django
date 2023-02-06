from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
path("products/", views.products, name= "product"),
path("cart/", views.cart_list, name= "cart_list"),
path("product/<pk>/", views.product, name= "product"),
path("deletecart/<pk>/", views.deletetfromcart, name= "deletefromcart"),
path("updatecart/<pk>/", views.updatecart, name= "updatecart"),


]