# Generated by Django 2.2.9 on 2020-02-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20200202_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mainimage',
            field=models.ImageField(blank=True, upload_to='inventory/images/'),
        ),
    ]