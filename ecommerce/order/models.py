from django.contrib.auth.models import User
from django.db import models
from product.models import Product  

class Order(models.Model):
    user = models.ForeignKey(User, related_name = "orders", on_delete = models.CASCADE)
    first_name = models.CharFields(max_length=100)
    last_name = models.CharFields(max_length=100)
    email = models.CharFields(max_length=100)
    address = models.CharFields(max_length=100)
    zipcode = models.CharFields(max_length=100)
    place = models.CharFields(max_length=100)
    phone = models.CharFields(max_length=100)
    created_at =models.DateTimeField(auto_now_add = True)
    paid_amound = models.DecimalField(max_digit=8, decimal_phaces=2, black=True, null = True)
    stripe_token = models.CharField(max_length = 150)
    
    def Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.first_name

class OrderItem(models.Model):
    order =  models.ForeignKey(Order, related_name = "items", on_delete = models.CASCADE)
    product = models.ForeignKey(Product, related_name = "items", on_delete = models.CASCADE)
    price = models.DecimalField(max_digit=8, decimal_phaces=2, black=True, null = True)
    quantity = models.IntegerField(default = 1)
    
    def __str__(self):
        return '%s' %s self.id