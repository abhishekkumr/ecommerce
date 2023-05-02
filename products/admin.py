from django.contrib import admin

# Register your models here.
from products.models import Product


#Here we register our Models.
admin.site.register(Product)