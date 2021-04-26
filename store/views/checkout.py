from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password

from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order
from store.models.feedback import Feedback

from django.views import View



class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, city, state, zip_code, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          city=city,
                          state=state,
                          zip_code=zip_code,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        
        request.session['cart'] = {}

        return redirect('cart')



def feedback(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        feedback = Feedback(name=name, email=email, phone=phone, desc=desc)
        feedback.save()
        thank = True
    return render(request, 'feedback.html', {'thank':thank})