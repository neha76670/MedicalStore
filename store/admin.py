from django.contrib import admin
from .models import Product, Category, Customer, Order, Feedback


#For Showing in admin Panel

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'description']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']


class AdminOrder(admin.ModelAdmin):
    list_display = ['customer', 'address', 'phone', 'price', 'date', 'status']


class AdminFeedback(admin.ModelAdmin):
    list_display = ['msg_id', 'name', 'email']

# Register your models here.

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)
admin.site.register(Feedback, AdminFeedback)
