# Generated by Django 5.0.4 on 2024-04-04 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category_name'], 'verbose_name_plural': 'Category'},
        ),
    ]
