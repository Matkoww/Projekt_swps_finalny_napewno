from django.contrib import admin

# Register your models here.
from .models import Product, Category, Order, Review

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Review)
