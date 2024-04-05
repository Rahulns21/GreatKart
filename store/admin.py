from django.contrib import admin
from django.utils.html import format_html
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html("<img src='{}' width='50' style='border-radius: 5px;' />".format(object.images.url))

    thumbnail.short_description = 'Image'

    list_display = ('product_name', 'thumbnail', 'price', 'stock',
                    'is_available', 'category', 'created_date', 'modified_date')
    list_display_links = ('product_name',)
    search_fields = ('product_name', 'category__category_name')
    list_per_page = 25


admin.site.register(Product, ProductAdmin)
