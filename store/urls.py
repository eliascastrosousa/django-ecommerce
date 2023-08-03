from django.urls import path, include
from .views import home, productpage, cart, checkout,books, eletronics

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('books/', books, name='books'),
    path('eletronics/', eletronics, name='eletronics'),
    path('productpage/<int:id>', productpage, name='productpage' ),
    path('cart/', cart, name='cart' ),
    path('checkout/', checkout, name='checkout' )
]