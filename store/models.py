from django.db import models
from autoslug import AutoSlugField
from djmoney.models.fields import MoneyField
from category.models import Category
from django.urls import reverse

class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_date']

    def __str__(self) -> str:
        return self.product_name
    
    # Update slug if product_name has changed
    def save(self, *args, **kwargs):
        if self.product_name and self.slug != self.product_name:
            self.slug = self.product_name
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('store:products-detail', args=[self.category.slug, self.slug])

    product_name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='product_name', unique=True)
    product_description = models.TextField(max_length=500, blank=True)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='INR')
    discount_price = MoneyField(max_digits=14, decimal_places=2, default_currency='INR', null=True, blank=True)
    images = models.ImageField(upload_to='images/products')
    stock = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)
    
    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)

variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
)
class Variation(models.Model):
    class Meta:
        verbose_name = 'Variation'
        verbose_name_plural = 'Variations'

    def __str__(self):
        return self.variation_value

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    objects = VariationManager()