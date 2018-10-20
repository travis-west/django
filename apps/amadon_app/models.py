from __future__ import unicode_literals
from django.db import models

# could not figure out how to call this from the views page
class ProductManager(models.Manager):
    def calculateTotal(self, id, qty):
        product = self.get(id=id)
        total_cost = float(product.price) * float(qty) 

        return total_cost


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ProductManager()

    def __repr__(self):
        return "<Product object: {} {}>".format(self.id, self.name)
