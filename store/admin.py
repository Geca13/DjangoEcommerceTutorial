from django.contrib import admin
from django.db import models
from.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date')
    prepopulated_fields = {'slug':('product_name',)}


admin.site.register(Product,ProductAdmin)

