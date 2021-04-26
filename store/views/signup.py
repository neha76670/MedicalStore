from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password

#from store.models.product import Product
#from store.models.category import Category
from store.models.customer import Customer

from django.views import View


class Signup(View):

    def get(self, request):

        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # Validating
        value = {
                'first_name' : first_name,
                'last_name' : last_name,
                'phone' : phone,
                'email' : email
        }

        error_message = None

        customer = Customer(first_name = first_name,
                                last_name = last_name,
                                phone = phone,
                                email = email,
                                password = password )

        error_message = self.validateCustomer(customer)

        if(not error_message):
            print(first_name, last_name, phone, email, password)
            
            # For Password 
            customer.password = make_password(customer.password)
            
            customer.register()

            return redirect('homepage')
        else:
            data = {
                    'error' : error_message,
                    'values' : value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None

        if(not customer.first_name):
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = "First Name must be 4 Charcter long "
            
        elif not customer.last_name:
            error_message = "Last Name Required !!"
        elif len(customer.last_name) < 4:
            error_message = "Last Name must be 4 Char long "
            
        elif not customer.phone:
            error_message = "Phone Number Required !!"
        elif len(customer.phone) < 10:
            error_message = "Phone Number must be 10 digits "

        elif len(customer.email) < 6:
            error_message = "Email must required !! "

        elif len(customer.password) < 5:
            error_message = "Password must be minimum 5 charcter "

        elif customer.isExists():
            error_message = "Email Already Register.."

        return error_message
