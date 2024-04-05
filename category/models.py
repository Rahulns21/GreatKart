from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Category'
        ordering = ['category_name']

    def __str__(self) -> str:
        return self.category_name
    
    # Update slug if category_name has changed
    def save(self, *args, **kwargs):
        if self.category_name and self.slug != self.category_name:
            self.slug = self.category_name
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('store:products-by-category', args=[self.slug])

    category_name = models.CharField(max_length=50, unique=True)
    slug = AutoSlugField(populate_from='category_name', unique=True)
    description = models.TextField(max_length=255, blank=True)
    category_image = models.ImageField(upload_to='images/categories', blank=True)