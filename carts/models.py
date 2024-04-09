from django.db import models
from store.models import Product, Variation

class Cart(models.Model):
    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Cart'
        ordering = ['-date_added']

    def __str__(self) -> str:
        return self.cart_id

    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

class CartItem(models.Model):
    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'

    def __unicode__(self) -> str:
        return self.product
    
    def sub_total(self):
        return self.product.price * self.quantity

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    variations = models.ManyToManyField(Variation, blank=True)