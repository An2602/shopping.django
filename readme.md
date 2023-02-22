<!-- create product app -->
# create class Product in DB:
# name
# description
# price
# image

# create class CartItem in DB and make a foreign key to Product:
# product (FK)
# quantity

# put both classes in admin.py

<!-- create serializer.py -->
# create class ProductSerializer
# create class CartSerializer and connect it to ProductSerializer
# create class CartSerializertwo

<!-- in views -->
# create products @api_view(['GET', 'POST']) and connect it to Product and use ProductSerializer
# create product @api_view(['DELETE', 'PUT','GET']) and connect it to Product and use ProductSerializer
# create cart_list @api_view(['GET', 'POST']) and connect it to CartItem and use CartSerializer and CartSerializertwo
# create deletetfromcart @api_view(['DELETE', ]) and connect it to CartItem
# create updatecart @api_view(['PUT', ]) and connect it to CartItem and use CartSerializertwo

<!-- in urls -->
# create products/ path and connect it to views.products
# create cart/ path and connect it to views.cart_list
# create product/<pk>/ path and connect it to views.product
# create deletecart/<pk>/ path and connect it to views.deletefromcart
# create updatecart/<pk>/ path and connect it to views.updatecart