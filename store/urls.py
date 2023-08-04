from django.urls import path, include
from .views import home, productpage, cart, checkout,books, telefonia, moveis, eletrodomesticos

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('books/', books, name='books'),
    path('telefonia/', telefonia, name='telefonia'),
    path('moveis/', moveis, name='moveis'),
    path('eletrodomesticos/', eletrodomesticos, name='eletrodomesticos'),
    path('productpage/<int:id>', productpage, name='productpage' ),
    path('cart/', cart, name='cart' ),
    path('checkout/', checkout, name='checkout' )
]