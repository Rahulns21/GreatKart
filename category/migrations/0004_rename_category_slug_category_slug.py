# Generated by Django 5.0.4 on 2024-04-04 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_rename_slug_category_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_slug',
            new_name='slug',
        ),
    ]