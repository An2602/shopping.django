from django.urls import path
from . import views 

app_name = 'product'

urlpatterns = [
    path('product/', views.products, name= "product"),
    path('cartitem/', views.cartitem, name= "cartitem"),
    # path('product/<pk>', views.product, name= "product"),
    # path('update/<pk>/', views.update_product, name="edit"),
    # path('delete/<pk>/', views.delete_product, name="delete")

]
