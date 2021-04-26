from django.contrib import admin
from django.urls import path

from .views.home import Index, store
from .views.login import Login, logout, mainpage, footer, about
from .views.signup import Signup
from .views.cart import Cart
from .views.checkout import CheckOut, feedback
from .views.orders import OrderView

from .middlewares.auth import auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store/', store, name= 'store'),

    path('signup/', Signup.as_view(), name='signup'),

    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name= 'logout'),
    path('mainpage/', mainpage, name= 'mainpage'),
    path('footer/', footer, name= 'footer'),
    path('about/', about, name= 'about'),

    path('cart/', auth_middleware(Cart.as_view()), name='cart'),

    path('check-out/', CheckOut.as_view(), name='checkout'),
    path('feedback/', feedback, name= 'feedback'),

    path('orders/', auth_middleware(OrderView.as_view()), name='orders'),
]
