# Generated by Django 2.2.9 on 2020-02-02 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_cart_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
