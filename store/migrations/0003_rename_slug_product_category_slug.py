# Generated by Django 5.0.4 on 2024-04-04 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_options_product_discount_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='slug',
            new_name='category_slug',
        ),
    ]
