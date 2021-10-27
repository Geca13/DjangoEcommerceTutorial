from django.db import models
from account.models import Account
from store.models import Product, Variation

class Pay(models.Model):
    
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    amount_paid = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    user: models.ForeignKey(Account , on_delete=models.CASCADE)

    def __str__(self):
        return self.payment_id

class Ord(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelle'),
    )     
    
    order_number = models.CharField(max_length=20, null=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    order_note = models.CharField(max_length=100)
    order_total = models.FloatField()
    tax = models.FloatField()
    status = models.CharField(max_length=15, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #user: models.ForeignKey(User , on_delete=models.SET_NULL, null=True)
    payment: models.ForeignKey(Pay , on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.first_name


class OrdProduct(models.Model):
    
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price =  models.FloatField()
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    order: models.ForeignKey(Ord , on_delete=models.CASCADE)
    payment: models.ForeignKey(Pay , on_delete=models.SET_NULL, null=True, blank=True)
    #user: models.ForeignKey(User , on_delete=models.CASCADE)
    product: models.ForeignKey(Product , on_delete=models.CASCADE)
    variation: models.ForeignKey(Variation , on_delete=models.CASCADE)

    def __str__(self):
        return self.product.product_name
     



